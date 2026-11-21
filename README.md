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

## Latest list — 2026-11-21 07:21 UTC

New packages created between 2026-11-21 06:19 UTC and 2026-11-21 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T07-21-20-005009Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 06:30:34 | [Minanggadang](https://www.nuget.org/packages/Minanggadang) | 1.0.0 | Minang Gadang — Restoran Pada… | Minang Gadang Padang restaurant Tanah Abang constants. Official: https://minang… |
| 2026-11-21 06:38:14 | [Sud.Gip.Auth](https://www.nuget.org/packages/Sud.Gip.Auth) | 1.0.0 | Sud.Gip.Auth | Standalone Sud GIP HS256 authentication SDK for .NET. |
| 2026-11-21 06:44:56 | [WinformUi](https://www.nuget.org/packages/WinformUi) | 1.0.0 | maqiul | Fluent Design style controls for Windows Forms. Supports .NET Framework 4.8 and… |
| 2026-11-21 06:46:45 | [z3l.FastHtmlParser.HtmlToMarkdown](https://www.nuget.org/packages/z3l.FastHtmlParser.HtmlToMarkdown) | 1.6.1 | z3l | Fast HTML to Markdown converter for .NET 9/10, built on z3l.FastHtmlParser: 10–… |
| 2026-11-21 06:52:53 | [LinKit.Engine.Microservice](https://www.nuget.org/packages/LinKit.Engine.Microservice) | 4.1.0 | Linh Nguyen | Bundle: installs the complete LinKit stack for a service (CQRS, endpoints, back… |
| 2026-11-21 06:52:55 | [LinKit.Engine.Monolith](https://www.nuget.org/packages/LinKit.Engine.Monolith) | 4.1.0 | Linh Nguyen | Bundle: installs the complete in-process LinKit stack (CQRS, endpoints, backgro… |
| 2026-11-21 06:57:48 | [Mango.EntityFrameworkCore](https://www.nuget.org/packages/Mango.EntityFrameworkCore) | 1.0.0 | Mango.CodeTransfer | Exports the supplied Avalonia project files on explicit request. |
| 2026-11-21 06:58:06 | [PageAssay](https://www.nuget.org/packages/PageAssay) | 0.1.0 | iyulab | Checks a web page without AI: drives it over the Chrome DevTools Protocol, coll… |
| 2026-11-21 06:59:07 | [Tubatools.PeripheralBattery](https://www.nuget.org/packages/Tubatools.PeripheralBattery) | 1.2.2 | 蔡先生 | 在图吧工具箱里读取无线键鼠电量，并可通过无线调试显示作为副屏的安卓手机/平板电量，均不需要厂商驱动常驻。 |
| 2026-11-21 07:04:55 | [PicVane.PaletteDistance](https://www.nuget.org/packages/PicVane.PaletteDistance) | 0.1.0 | js-upup | Find the closest entry in an ordered eight-bit RGB palette. Source-only C# cont… |
| 2026-11-21 07:14:49 | [Pkcs10](https://www.nuget.org/packages/Pkcs10) | 1.0.0 | Matthew J. Bobowski | A native .NET PKCS #10 certificate signing request parser and validator using S… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
