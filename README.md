# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 03:20 UTC

New packages created between 2026-11-02 02:18 UTC and 2026-11-02 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T03-20-06-242319Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 02:20:22 | [Juice.OpenTelemetry](https://www.nuget.org/packages/Juice.OpenTelemetry) | 10.8.0 | Creatorflow.io | OpenTelemetry integration for Juice: registers the Juice ActivitySource and Met… |
| 2026-11-02 02:22:07 | [Cangming.PicoPlugins.Sandbox](https://www.nuget.org/packages/Cangming.PicoPlugins.Sandbox) | 0.1.3.1102 | Fangyu | 仅组织内部使用。插件沙箱侧客户端：把沙箱进程内的插件能力经协议面暴露给宿主。 |
| 2026-11-02 02:22:12 | [Cangming.PicoPlugins.Sandbox.Contracts](https://www.nuget.org/packages/Cangming.PicoPlugins.Sandbox.Contracts) | 0.1.3.1102 | Fangyu | 仅组织内部使用。插件沙箱两侧共用的协议面：不引用内核，宿主侧与沙箱侧各自实现。 |
| 2026-11-02 02:22:16 | [Cangming.PicoPlugins.SandboxHost](https://www.nuget.org/packages/Cangming.PicoPlugins.SandboxHost) | 0.1.3.1102 | Fangyu | 仅组织内部使用。插件沙箱宿主进程：承载被隔离装载的插件。 |
| 2026-11-02 02:23:08 | [Fanuc.RobotInterface.Extensions](https://www.nuget.org/packages/Fanuc.RobotInterface.Extensions) | 3.0.4 | Victor Tseng | Open source implentation for Fanuc RobotInterface. |
| 2026-11-02 02:23:33 | [Fanuc.SRTP](https://www.nuget.org/packages/Fanuc.SRTP) | 3.0.4 | Victor Tseng | Open source implentation for Fanuc RobotInterface. |
| 2026-11-02 02:33:09 | [OfdNet.Archive](https://www.nuget.org/packages/OfdNet.Archive) | 0.1.1 | icysky | OFD-A 合规检查（23 条规则）与转换（23 个处理器）。 |
| 2026-11-02 02:33:10 | [OfdNet.Core](https://www.nuget.org/packages/OfdNet.Core) | 0.1.1 | icysky | OFD 数据模型：文档结构、页面、图元、字体、签名、注释与动作。 |
| 2026-11-02 02:33:11 | [OfdNet.Crypto](https://www.nuget.org/packages/OfdNet.Crypto) | 0.1.1 | icysky | OFD 加密/解密（口令、证书、FEK）。 |
| 2026-11-02 02:33:12 | [OfdNet.Font](https://www.nuget.org/packages/OfdNet.Font) | 0.1.1 | icysky | OFD 字体度量（SkiaSharp）与宽度映射表；包含 Noto Serif SC（OFL）。 |
| 2026-11-02 02:33:13 | [OfdNet.Gm](https://www.nuget.org/packages/OfdNet.Gm) | 0.1.1 | icysky | 国密结构：SM2/SM3、国密证书与 SES 结构。 |
| 2026-11-02 02:33:14 | [OfdNet.Layout](https://www.nuget.org/packages/OfdNet.Layout) | 0.1.1 | icysky | OFD 排版引擎：Div 树、分段、虚拟页面与页面图元。 |
| 2026-11-02 02:33:15 | [OfdNet.Pkg](https://www.nuget.org/packages/OfdNet.Pkg) | 0.1.1 | icysky | OFD 虚拟容器（OFDDir/DocDir/PagesDir/ResDir）与打包解包。 |
| 2026-11-02 02:33:16 | [OfdNet.Reader](https://www.nuget.org/packages/OfdNet.Reader) | 0.1.1 | icysky | OFD 读取、资源定位、内容抽取、关键字检索与旧版读取器。 |
| 2026-11-02 02:33:17 | [OfdNet.Sign](https://www.nuget.org/packages/OfdNet.Sign) | 0.1.1 | icysky | OFD 数字签名、签章与验签（GB/T 35275、SES V1/V4/V5）。 |
| 2026-11-02 02:33:17 | [OfdNet.Tool](https://www.nuget.org/packages/OfdNet.Tool) | 0.1.1 | icysky | OFD 工具：文档合并、页面删除、裸文档构造。 |
| 2026-11-02 02:33:18 | [OfdNet](https://www.nuget.org/packages/OfdNet) | 0.1.1 | icysky | OfdNet 元包：一次安装 OFD 读取、编辑、排版、签章、加密、OFD-A 与合并全部模块。 |
| 2026-11-02 02:34:28 | [HandlerPipe](https://www.nuget.org/packages/HandlerPipe) | 1.0.6 | Luigi Llerena | Librería ligera para manejo explícito de comandos/queries y pipelines de ejecuc… |
| 2026-11-02 02:35:31 | [VS_Builder.MSBuildAnalyzer](https://www.nuget.org/packages/VS_Builder.MSBuildAnalyzer) | 1.0.2 | Olexander | MSBuild Compatibility Analyzer - inspect MSBuild files, toolset versions, and b… |
| 2026-11-02 03:10:18 | [SpaceWizards.NetSerializer](https://www.nuget.org/packages/SpaceWizards.NetSerializer) | 1.0.0 | Tomi Valkeinen,Space Wizards… | A very fast and minimal serializer |
| 2026-11-02 03:14:34 | [ProjectZ.Linux](https://www.nuget.org/packages/ProjectZ.Linux) | 2026.11.1.1 | Project-Z | Project-Z scenes, native XAML, controls, vector text and GPU effects using Mono… |
| 2026-11-02 03:14:35 | [ProjectZ.macOS](https://www.nuget.org/packages/ProjectZ.macOS) | 2026.11.1.1 | Project-Z | Project-Z scenes, native XAML, controls, vector text and GPU effects using Mono… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
