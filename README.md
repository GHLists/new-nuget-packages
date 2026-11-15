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

## Latest list — 2026-11-15 12:21 UTC

New packages created between 2026-11-15 11:21 UTC and 2026-11-15 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T12-21-46-275061Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 11:23:31 | [EfMigrationLint](https://www.nuget.org/packages/EfMigrationLint) | 0.2.0 | EF Migration Lint contributors | Source-only checks for potentially destructive EF Core migration operations. Re… |
| 2026-11-15 11:41:36 | [ClipboardMonitor.Quiet](https://www.nuget.org/packages/ClipboardMonitor.Quiet) | 3.0.0 | davpnuser,JPS | A fork of ClipboardMonitor.Core without the built-in "Debugging" console writes… |
| 2026-11-15 11:50:31 | [Sagynbaev.Tessera.Agents](https://www.nuget.org/packages/Sagynbaev.Tessera.Agents) | 5.1.0 | Azimbek Sagynbaev | Verified-agent identity for Tessera: issue/verify an agent_identity attestation… |
| 2026-11-15 11:57:14 | [Sky1sBloo.VzSocketReceiver](https://www.nuget.org/packages/Sky1sBloo.VzSocketReceiver) | 1.0.0 | Sky1sBloo | Library for receiving and sending data to Juno: New Origins via the Sockets ser… |
| 2026-11-15 12:01:50 | [CifroArts.SimplifiedCSharp.Style](https://www.nuget.org/packages/CifroArts.SimplifiedCSharp.Style) | 1.0.0 | CifroArts | CifroArts C# code style: Roslyn analyzers and code fixes for Unity and .NET pro… |
| 2026-11-15 12:06:27 | [GCR.Host](https://www.nuget.org/packages/GCR.Host) | 0.1.2 | GCR | 宿主：Blazor Server 管理界面与 Minimal API，单进程单端口。可经 NuGet 引用后由外部宿主用 builder.AddGCR() /… |
| 2026-11-15 12:06:38 | [GCR.Licensing](https://www.nuget.org/packages/GCR.Licensing) | 0.1.2 | GCR | GCR.Framework 离线 License：RSA 非对称签名与验签（公钥随框架分发，私钥由厂商自持） |
| 2026-11-15 12:06:40 | [GCR.Presentations.Admin.Information](https://www.nuget.org/packages/GCR.Presentations.Admin.Information) | 0.1.2 | GCR | Admin 模块表现层：information 能力域的信息管理统一渲染 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
