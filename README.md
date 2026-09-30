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

## Latest list — 2026-09-30 08:20 UTC

New packages created between 2026-09-30 07:22 UTC and 2026-09-30 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T08-20-43-898782Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 07:32:15 | [ProduceSelf.ClientSdk.Ops](https://www.nuget.org/packages/ProduceSelf.ClientSdk.Ops) | 0.1.2 | 沧海的频道 | 诺元运维平台客户端 SDK（A 档）：设备注册与心跳、日志采集上报、崩溃补报、下行指令（SetLogLevel / PullLogFile / Collect… |
| 2026-09-30 07:37:38 | [Syncfusion.Maui.Diagram](https://www.nuget.org/packages/Syncfusion.Maui.Diagram) | 35.1.37 | Syncfusion® Inc. | This package provides the functionality to utilize the features of Syncfusion®… |
| 2026-09-30 07:43:15 | [NotoriousTest.Dependencies.Azure.FunctionCoreTools](https://www.nuget.org/packages/NotoriousTest.Dependencies.Azure.FunctionCoreTools) | 5.1.0 | Brice SCHUMACHER | Azure Functions Core Tools dependency for NotoriousTest infrastructures. |
| 2026-09-30 07:43:21 | [NotoriousTest.Requirements.Docker](https://www.nuget.org/packages/NotoriousTest.Requirements.Docker) | 5.1.0 | Brice SCHUMACHER | Docker requirement for NotoriousTest infrastructures. |
| 2026-09-30 07:43:24 | [NotoriousTest.Web.AzureFunctions](https://www.nuget.org/packages/NotoriousTest.Web.AzureFunctions) | 5.1.0 | Brice SCHUMACHER | Azure functions integration tests support for NotoriousTest. |
| 2026-09-30 07:55:49 | [EngineeringFluids](https://www.nuget.org/packages/EngineeringFluids) | 0.1.3 | Mads Kirk Foged | Fast, unit-typed thermodynamic and transport properties for engineering fluids… |
| 2026-09-30 08:02:42 | [NibblePoker.Win32.Mailslot](https://www.nuget.org/packages/NibblePoker.Win32.Mailslot) | 0.0.8 | NibblePoker,Herwin Bozet | A simple and 'to-the-point' library to parse launch arguments in .NET and .NET… |
| 2026-09-30 08:04:47 | [Semi.Avalonia.MediaPlayer](https://www.nuget.org/packages/Semi.Avalonia.MediaPlayer) | 1.0.0 | IRIHI Technology Co., Ltd. | Avalonia.Controls.MediaPlayer themes inspired by Semi Design. |
| 2026-09-30 08:05:07 | [Bimwright.Nwd.Server](https://www.nuget.org/packages/Bimwright.Nwd.Server) | 1.0.0 | Khoa Le | MCP gateway for Autodesk Navisworks Manage 2022-2027. |
| 2026-09-30 08:08:12 | [TenonAdmin.Workflow](https://www.nuget.org/packages/TenonAdmin.Workflow) | 0.7.0 | huguodong | TenonAdmin 工作流可选包:审批定义/引擎/待办与设计器配套 API;AddTenonAdminWorkflow + UseWorkflow 启用(T… |
| 2026-09-30 08:08:13 | [TenonAdmin.Integration](https://www.nuget.org/packages/TenonAdmin.Integration) | 0.7.0 | huguodong | TenonAdmin 第三方接入可选包:接入应用与 API Key、开放接口授权与数据范围、出站调用与可靠投递;AddTenonAdminIntegratio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
