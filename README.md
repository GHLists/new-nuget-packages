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

## Latest list — 2026-10-03 10:19 UTC

New packages created between 2026-10-03 09:20 UTC and 2026-10-03 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T10-19-26-317855Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 09:27:09 | [Bladehero.Telegram.Platform.Conversations.EntityFrameworkCore](https://www.nuget.org/packages/Bladehero.Telegram.Platform.Conversations.EntityFrameworkCore) | 10.4.0 | bladehero | An Entity Framework Core store for the conversations of Telegram bots built on… |
| 2026-10-03 09:33:52 | [RibbonSpace.WinUI](https://www.nuget.org/packages/RibbonSpace.WinUI) | 1.1.0 | Wiesław Šoltés | Professional Office-style Ribbon for WinUI 3 (Windows App SDK): classic and sim… |
| 2026-10-03 09:33:52 | [Cosmos.Network.Http](https://www.nuget.org/packages/Cosmos.Network.Http) | 2.0.0 | Cosmos | HTTP client for Cosmos Gen3 kernels. |
| 2026-10-03 09:55:11 | [ChudoObuv.DemoExam2027.Template](https://www.nuget.org/packages/ChudoObuv.DemoExam2027.Template) | 1.0.0 | ChudoObuv | Шаблон решения «Чудо Обувь» (WPF .NET 8 + MS SQL Server): исходный код, скрипт… |
| 2026-10-03 09:58:48 | [Aore.Excel](https://www.nuget.org/packages/Aore.Excel) | 1.0.0 | WEI.ZHOU (Willis) | 高性能,纯托管 .xlsx 读写库 |
| 2026-10-03 10:00:56 | [FS.GG.SDD.Knowledge](https://www.nuget.org/packages/FS.GG.SDD.Knowledge) | 2.1.0 | FS.GG | Concise Git-backed project findings with shared capture, retrieval and history… |
| 2026-10-03 10:03:43 | [Automa](https://www.nuget.org/packages/Automa) | 1.0.0 | Tezzz | An interpreter for Automating tasks around your computer. |
| 2026-10-03 10:10:09 | [RonSijm.Blazyload.Components.SourceGenerator](https://www.nuget.org/packages/RonSijm.Blazyload.Components.SourceGenerator) | 1.1.0 | Ron Sijm | Generate component identifiers and automatically export shared models into comp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
