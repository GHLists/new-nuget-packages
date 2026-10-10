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

## Latest list — 2026-10-10 20:21 UTC

New packages created between 2026-10-10 19:20 UTC and 2026-10-10 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T20-21-57-307077Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 19:25:03 | [NuvTools.Security.Biometrics.Serpro](https://www.nuget.org/packages/NuvTools.Security.Biometrics.Serpro) | 10.0.0 | Nuv Tools | SERPRO Datavalid implementation of the NuvTools.Security facial verification co… |
| 2026-10-10 19:25:12 | [NuvTools.Security.Certificate.Lacuna](https://www.nuget.org/packages/NuvTools.Security.Certificate.Lacuna) | 10.0.0 | Nuv Tools | Lacuna REST PKI implementation of the NuvTools.Security certificate authenticat… |
| 2026-10-10 19:33:15 | [DaffyReplay](https://www.nuget.org/packages/DaffyReplay) | 0.1.0 | TroBeeOne LLC | Replays a DaffyTee recording of real SQL Server traffic against a test or pre-p… |
| 2026-10-10 19:34:53 | [exuarch](https://www.nuget.org/packages/exuarch) | 1.40.0 | olebru | Check, assemble and run ExuArch machine packages from the command line: the mac… |
| 2026-10-10 19:49:23 | [KestrelAcme](https://www.nuget.org/packages/KestrelAcme) | 0.1.0 | KestrelAcme contributors | Automatic HTTPS for ASP.NET Core: issues and renews Let's Encrypt (ACME) certif… |
| 2026-10-10 19:51:10 | [SharpCell.Grid.Avalonia](https://www.nuget.org/packages/SharpCell.Grid.Avalonia) | 0.1.0 | Mark Shvabenlandt | Excel-like spreadsheet control for Avalonia UI that shows SharpCell workbooks.… |
| 2026-10-10 19:51:11 | [SharpCell.Grid](https://www.nuget.org/packages/SharpCell.Grid) | 0.1.0 | Mark Shvabenlandt | Excel-like spreadsheet grid for SharpCell workbooks, independent of any UI fram… |
| 2026-10-10 19:53:23 | [Elarion.EntityFrameworkCore.LeasedWork](https://www.nuget.org/packages/Elarion.EntityFrameworkCore.LeasedWork) | 0.2.12 | Simon Wimmesberger | EF Core leased work rows for Elarion (ADR-0073): a provider-neutral claim / lea… |
| 2026-10-10 19:53:25 | [Elarion.AspNetCore.ProxyIdentity](https://www.nuget.org/packages/Elarion.AspNetCore.ProxyIdentity) | 0.2.12 | Simon Wimmesberger | Optional ASP.NET Core authentication for Elarion apps behind an authenticating… |
| 2026-10-10 19:56:55 | [Pz.Connector.ClickHouse](https://www.nuget.org/packages/Pz.Connector.ClickHouse) | 0.1.0 | PipelineZ contributors | ClickHouse source and sink connector for PipelineZ (pz), served out of process:… |
| 2026-10-10 20:01:48 | [Raffinert.Expressions.EntityFrameworkCore](https://www.nuget.org/packages/Raffinert.Expressions.EntityFrameworkCore) | 1.2.0 | Yevhen Cherkes | EF Core 10 async condition operators and opt-in expression expansion before nat… |
| 2026-10-10 20:03:23 | [Soenneker.Esbuild.Util](https://www.nuget.org/packages/Soenneker.Esbuild.Util) | 4.0.1 | Jake Soenneker | A C# utility for installing and running esbuild builds, transforms, and increme… |
| 2026-10-10 20:07:00 | [Yukat.UpdateVerify](https://www.nuget.org/packages/Yukat.UpdateVerify) | 0.2.0 | MinoriSama | Verify RSA-PSS signed update metadata, expiry and local package integrity. |
| 2026-10-10 20:08:48 | [Yukat.UpdateVerify.Tool](https://www.nuget.org/packages/Yukat.UpdateVerify.Tool) | 0.2.0 | MinoriSama | Verify signed update metadata and local package integrity without execution. |
| 2026-10-10 20:11:54 | [Rhino.Scripting.QrCode](https://www.nuget.org/packages/Rhino.Scripting.QrCode) | 0.2.0 | GoswinR | Create QR codes as Rhino3D Meshes or Hatches, using ZXing.Net |
| 2026-10-10 20:13:04 | [2dog.repl](https://www.nuget.org/packages/2dog.repl) | 4.7.2.112 | Moritz Voss | A terminal C# REPL inside a running Godot engine, with completion, highlighting… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
