---
title: conda和uv 常用命令
typora-root-url: ../../source
tags:
  - conda
  - python
categories: python
date: 2018-11-19 18:52:16
---

# uv命令

# conda命令

- 创建虚拟环境

```shell
conda create -n your_env_name python=x.x anaconda
```

最后的anaconda可选，有的话，会安装很多包，numpy、sklearn等等
- 激活

```shell
source activate your_env_name
```

- 安装包

```shell
conda install -n your_env_name [package]
```

- 不激活

```shell
source deactivate
```

- 已经有的虚拟环境

```shell
conda env list
```

- 删除虚拟环境

```shell
conda remove -n your_env_list -all
```

- 检查conda是否安装

```shell
conda -v
```

- 更新conda

```shell
conda update conda
```

---

# 为什么要用uv

Python 项目管理从传统的 `pip` 演进到 Conda 或 UV 等现代工具，主要围绕解决环境隔离、依赖冲突、以及依赖关系的可维护性等痛点展开。

以下是基于提供的资料，梳理的 Python 项目管理现代化的演进过程和主要流派：

## 传统的 pip 安装和环境冲突 (早期的痛点)

Python 在诞生之初，并未考虑工程结构的问题，导致早期的管理相当“放自我”。官方的 `pip` 规范一直在努力打补丁。

1. **全局环境与冲突：** 在项目初期，使用 `pip install flask` 等命令会将库安装到一个**全局环境**中，被计算机上所有 Python 项目共享。
2. **版本冲突：** 这种共享机制带来棘手的问题，例如一个新项目可能需要 Flask 3.11，而另一个旧项目可能只兼容 3.0，导致全局升级后旧项目无法运行。
3. **依赖地狱：** 库通常依赖其他几个库，这些库又有各自的依赖，层层嵌套会引发更多的版本冲突，即所谓的“依赖地狱”。

## 演进的第一步：环境隔离 (Venv)

为了解决版本和依赖冲突，设计出了**虚拟环境**（Virtual Environment）。

1. **Venv 的作用：** 虚拟环境为每个项目创建了一个独立、干净的 Python 工作空间。
2. **创建与激活：** 可以使用 `python -m venv .venv` 命令创建虚拟环境。激活环境后，再使用 `pip` 安装库，这些库就会被安装到该项目的虚拟文件夹中，从而避免冲突。
3. **背后的原理：** 虚拟环境主要通过修改 Python 中的 `sys.path` 变量来实现。激活环境后，虚拟目录会被添加到这个搜索列表里，确保 Python 在导入模块时能够成功加载安装在虚拟环境路径中的库。

## 演进的第二步：依赖共享与配置 (requirements.txt 到 pyproject.toml)

解决了环境隔离后，新的问题是如何方便准确地将项目的依赖列表分享给其他人，以便复现环境。

#### 1. requirements.txt (早期主流做法)

- **做法：** 早期最主流的做法是使用 `pip freeze` 命令，将当前虚拟环境中所有已安装包及其确切版本号输出到一个文件，通常命名为 `requirements.txt`。接收方只需执行 `pip install -r requirements.txt` 即可安装依赖。
- **重大缺陷：** `pip freeze` **无法区分**项目真正需要的**直接依赖**（Direct Dependency）和这些直接依赖引入的**间接依赖**（Indirect Dependency）。如果项目复杂，情况很快会失控。
- **孤儿依赖：** `pip` 在卸载包时也无法很好地处理依赖关系。如果卸载了某个包（如 Flask），那些因为 Flask 而被安装的间接依赖仍会留在环境中，成为无人管理的**孤儿依赖**。

#### 2. pyproject.toml (现代标准解决方案)

现代 Python 项目的**标准解决方案**是使用 `pyproject.toml` 文件。

- **统一配置：** `pyproject.toml` 是官方指定的统一配置文件。在此之前，不同的开发工具（如类型检查器 mypy、测试框架 pytest）通常使用各自独立的配置文件，导致根目录下配置零散。如今，绝大多数主流工具都支持了 `pyproject.toml`。
- **仅声明直接依赖：** 在 `pyproject.toml` 中，开发者只需在 `dependencies` 列表中声明项目的**直接依赖**即可。如果将来要删除某个依赖，只需删除配置文件中对应的一行，就不会留下任何孤儿依赖。
- **安装复杂性：** 依赖写好后，可以使用 `pip install .` 命令来安装。这条命令在背后做了两件事：首先是构建，将当前项目打包成标准 Python 软件包；其次是安装，自动把所有声明的依赖一并安装进来。
- **开发模式（Editable Mode）：** 在开发阶段，为了避免源代码被复制到虚拟环境中的 `site-packages` 目录导致代码修改无法同步，通常需要加上 `-e` 参数，使用 `pip install -e .` 进行可编辑安装。

## 演进的第三步：高级项目管理工具 (UV, Poetry)

纯手工维护 `pyproject.toml` 的流程存在痛点，例如无法再用简单的 `pip install` 命令添加新依赖，每次添加都需要手动查找名称和版本号并编辑配置，过程繁琐且容易出错。

1. **诞生原因：** 社区为解决这一痛点，催生了像 **UV** 和 **Poetry** 这样的高层项目管理工具。
2. **高级封装：** 这些第三方工具可以被理解为对 `venv` 和 `pip` 的**高级封装**。它们在底层仍使用 `venv` 和 `pip`，但提供了更简单、更统一的接口。
3. **UV 示例：** 使用 UV，只需执行 `uv add flask` 一条命令，就能自动修改 `pyproject.toml`（添加依赖声明）、自动创建 `venv` 虚拟环境，并将该包及其所有间接依赖安装到环境中。协作者只需执行 `uv sync`，即可自动读取配置文件、搭建环境并安装所有依赖。
4. **运行简化：** UV 还提供了 `uv run` 命令，可以在虚拟环境的上下文中执行命令，无需手动激活环境。

## 独立流派：Conda 宇宙

与官方 Python 体系并行的是 Conda 宇宙，这是一个从设计之初就考虑周全的跨语言开发平台。

1. **独立的生态：** Conda 最早由 Anaconda 公司提供，现在免费版 MiniConda 等使用更广泛，像 Pixi 也是这个生态的一部分。Conda 体系在底层上与官方 Python 走的不是一条路，它有自己的配置文件、软件仓库，甚至连 Python 解释器都是自己编译的。
2. **跨语言支持：** Conda 不只支持 Python，还支持 Go、Rust、C++、R 等各种语言。因此，它更像一个**独立的跨语言开发平台**。
3. **设计优势：** Conda 从设计之初就将多语言支持、依赖管理和虚拟环境等问题用一套统一的方案解决了。
4. **AI 领域的体现：** Conda 的优势在 AI 领域尤为明显，因为 AI 框架的依赖出了名的复杂，经常需要与 NVIDIA 的 CUDA 这种非 Python 库打交道。使用 Conda 安装深度学习框架通常是**最省心、最不容易出错的选择**。


