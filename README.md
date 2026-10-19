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

## Latest list — 2026-10-19 07:19 UTC

New packages created between 2026-10-19 06:21 UTC and 2026-10-19 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T07-19-31-526592Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 06:25:24 | [CodeBrix.RustTools.CrateBuilder.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.RustTools.CrateBuilder.MitLicenseForever) | 1.0.292.384 | Jeremy Ellis | A .NET library that turns a Rust crate into native binaries and a .NET 10 wrapp… |
| 2026-10-19 06:27:36 | [Reified.Schema.Testing](https://www.nuget.org/packages/Reified.Schema.Testing) | 0.11.0 | Adam Davies | [Experimental] FsCheck generators derived from Reified schemas, and seeded code… |
| 2026-10-19 06:27:37 | [Reified.SchemaGen.MSBuild](https://www.nuget.org/packages/Reified.SchemaGen.MSBuild) | 0.11.0 | Adam Davies | [Experimental] MSBuild integration for Reified schema generation: discovers [<D… |
| 2026-10-19 06:28:52 | [Axial.ElmishFlows](https://www.nuget.org/packages/Axial.ElmishFlows) | 0.11.0 | Adam Davies | [Incubating] Elmish integration for Axial flows: commands and subscriptions bac… |
| 2026-10-19 06:28:55 | [Axial.Files](https://www.nuget.org/packages/Axial.Files) | 0.11.0 | Adam Davies | [Incubating] Streaming file traversal and text reading for Axial workflows. |
| 2026-10-19 06:29:13 | [Axial.WebSocket](https://www.nuget.org/packages/Axial.WebSocket) | 0.11.0 | Adam Davies | [Experimental] Typed WebSocket client workflows for F#. |
| 2026-10-19 06:29:16 | [DecisionsDotNet.AI](https://www.nuget.org/packages/DecisionsDotNet.AI) | 0.2.0-preview | Adam Holm | Exposes any DecisionsDotNet IDecisionsClient (TypeSafe Jev, OpenRouter, or Open… |
| 2026-10-19 06:32:08 | [CxAgent.Plugins.Templates](https://www.nuget.org/packages/CxAgent.Plugins.Templates) | 0.9.37 | Nikolaos Protopapas | dotnet new cxagent-plugin — a cxagent plugin with its sidecar, a per-call gate… |
| 2026-10-19 06:32:09 | [CxAgent.Plugins.Testing](https://www.nuget.org/packages/CxAgent.Plugins.Testing) | 0.9.37 | Nikolaos Protopapas | Check and call a cxagent plugin from a test: the same loaders, gate and lifecyc… |
| 2026-10-19 06:35:07 | [Mud.Feishu.AI.Mcp](https://www.nuget.org/packages/Mud.Feishu.AI.Mcp) | 3.1.0 | Mud Studio | Mud.Feishu AI MCP server（可选包）：把已策展的飞书工具面（FeishuAgent:Tools / WriteAllowList 白名单… |
| 2026-10-19 06:35:09 | [Mud.Feishu.AI.Tools](https://www.nuget.org/packages/Mud.Feishu.AI.Tools) | 3.1.0 | Mud Studio | Mud.Feishu AI 飞书工具包：把 Bitable/Docx/Wiki/Search/IM/Sheets/Approval 接口经 [FeishuTo… |
| 2026-10-19 06:35:11 | [Mud.Feishu.AI](https://www.nuget.org/packages/Mud.Feishu.AI) | 3.1.0 | Mud Studio | Mud.Feishu AI-Native Agent 运行时：基于 Microsoft Agent Framework 的会话管理、模型接入与飞书工具执行链底… |
| 2026-10-19 06:42:05 | [Sentinel.Probes](https://www.nuget.org/packages/Sentinel.Probes) | 0.1.0 | A K M Muhibullah Nayem | Sentinel Dynamic Instrumentation for .NET: metric, span and span-tag probes pla… |
| 2026-10-19 06:51:37 | [ghver](https://www.nuget.org/packages/ghver) | 1.0.1 | Webbarrr | ghver — fetch the latest GitHub release information from the command line. |
| 2026-10-19 06:51:44 | [GeregeSystems.EidMongolia.Pades](https://www.nuget.org/packages/GeregeSystems.EidMongolia.Pades) | 0.3.0 | Gerege Systems LLC | eID Mongolia client-side PAdES for .NET (PDF never leaves the client): Prepare… |
| 2026-10-19 06:55:54 | [VikashKumar.XrmToolBox.DataQualityStudio](https://www.nuget.org/packages/VikashKumar.XrmToolBox.DataQualityStudio) | 1.2026.10.1 | Vikash Kumar | Dataverse Excel Mapping & Data Quality Studio: a configuration-driven import va… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
