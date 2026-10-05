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

## Latest list — 2026-10-05 06:21 UTC

New packages created between 2026-10-05 05:21 UTC and 2026-10-05 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T06-21-14-618382Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 05:47:50 | [M0LTE.RaptorQ](https://www.nuget.org/packages/M0LTE.RaptorQ) | 0.1.0 | packet-net | RaptorQ fountain code (RFC 6330) in managed C#: systematic encoding, repair sym… |
| 2026-10-05 05:50:12 | [SelectPdf.Universal.Native.win-x64](https://www.nuget.org/packages/SelectPdf.Universal.Native.win-x64) | 26.4.0 | SelectPdf | Platform-specific native engines for the SelectPdf.Universal and SelectPdf.Html… |
| 2026-10-05 05:52:52 | [SelectPdf.Universal.Native.win-x86](https://www.nuget.org/packages/SelectPdf.Universal.Native.win-x86) | 26.4.0 | SelectPdf | Platform-specific native engines for the SelectPdf.Universal and SelectPdf.Html… |
| 2026-10-05 05:53:43 | [PolyhydraGames.Streaming.Events](https://www.nuget.org/packages/PolyhydraGames.Streaming.Events) | 0.1.0.1 | PolyhydraGames.Streaming.Even… | Platform-neutral stream-event contracts. Dependency-light sibling of PolyhydraG… |
| 2026-10-05 05:55:56 | [SelectPdf.Universal.Native.linux-x64](https://www.nuget.org/packages/SelectPdf.Universal.Native.linux-x64) | 26.4.0 | SelectPdf | Platform-specific native engines for the SelectPdf.Universal and SelectPdf.Html… |
| 2026-10-05 05:58:07 | [SelectPdf.Universal.Native.linux-arm64](https://www.nuget.org/packages/SelectPdf.Universal.Native.linux-arm64) | 26.4.0 | SelectPdf | Platform-specific native engines for the SelectPdf.Universal and SelectPdf.Html… |
| 2026-10-05 06:00:12 | [SelectPdf.Universal.Native.osx-arm64](https://www.nuget.org/packages/SelectPdf.Universal.Native.osx-arm64) | 26.4.0 | SelectPdf | Platform-specific native engines for the SelectPdf.Universal and SelectPdf.Html… |
| 2026-10-05 06:01:07 | [SelectPdf.Universal.Fonts](https://www.nuget.org/packages/SelectPdf.Universal.Fonts) | 26.4.0 | SelectPdf | Google's Noto fonts (SIL Open Font License 1.1) for the SelectPdf.Universal and… |
| 2026-10-05 06:01:50 | [SelectPdf.Universal](https://www.nuget.org/packages/SelectPdf.Universal) | 26.4.0 | SelectPdf | SelectPdf is a cross-platform (Windows, Linux and macOS) PDF library for .NET t… |
| 2026-10-05 06:02:08 | [TypesafeSdk](https://www.nuget.org/packages/TypesafeSdk) | 0.1.0 | oliver-gc | Unofficial .NET client for the TypeSafe System One API. |
| 2026-10-05 06:02:09 | [SelectPdf.HtmlToPdf.Universal](https://www.nuget.org/packages/SelectPdf.HtmlToPdf.Universal) | 26.4.0 | SelectPdf | The free Community Edition of the SelectPdf HTML to PDF converter for .NET, fre… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
