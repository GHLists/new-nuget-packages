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

## Latest list — 2026-11-04 19:20 UTC

New packages created between 2026-11-04 18:19 UTC and 2026-11-04 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T19-20-08-462005Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 18:25:19 | [ReusableFiniteStateMachine.Release](https://www.nuget.org/packages/ReusableFiniteStateMachine.Release) | 0.1.6 | Aurélien Pascal Maignan | This library offer a reusable finite state machine (FSM) to use for your own pr… |
| 2026-11-04 18:25:26 | [ExcelReader.NET.Framework](https://www.nuget.org/packages/ExcelReader.NET.Framework) | 7.4.0 | Gabriel Matte | Fast XLSX/XLSB/XLS/CSV reading for .NET Framework 4.7.2+, backed by the ExcelRe… |
| 2026-11-04 18:27:52 | [Solhigson.Analyzers](https://www.nuget.org/packages/Solhigson.Analyzers) | 10.0.0 | Solhigson | Development-only compile-time rules for Solhigson projects: the IDE style rules… |
| 2026-11-04 18:30:12 | [WithEffect.Core](https://www.nuget.org/packages/WithEffect.Core) | 10.0.14 | WithEffect.Services | WithEffect.Core assembles well-known packages for rapid application prototyping… |
| 2026-11-04 18:51:14 | [WithEffect.Frontend](https://www.nuget.org/packages/WithEffect.Frontend) | 10.0.14 | WithEffect.Services | WithEffect.Core assembles well-known packages for rapid application prototyping… |
| 2026-11-04 18:54:37 | [Activout.Extensions.Configuration.Kdbx](https://www.nuget.org/packages/Activout.Extensions.Configuration.Kdbx) | 0.1.0 | Activout AB | A Microsoft.Extensions.Configuration source that reads secrets from a KeePass (… |
| 2026-11-04 18:59:20 | [Cartovia.Avalonia](https://www.nuget.org/packages/Cartovia.Avalonia) | 1.1.0 | Nicolas Estebe | Cartovia Avalonia map control: vector maps with MapLibre GL JS (no account need… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
