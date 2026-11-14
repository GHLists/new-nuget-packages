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

## Latest list — 2026-11-14 08:19 UTC

New packages created between 2026-11-14 07:18 UTC and 2026-11-14 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T08-19-58-779346Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 07:28:21 | [VL.PROJ](https://www.nuget.org/packages/VL.PROJ) | 0.0.1-alpha | VL.PROJ Contributors | EARLY - not ready for real work yet. Moves NetTopologySuite geometry from one c… |
| 2026-11-14 07:32:31 | [SafeSign.Formats](https://www.nuget.org/packages/SafeSign.Formats) | 1.2.0 | Glenn Watson and Contributors | File format signers for SafeSign: MSI, CAB, catalogs, APPX/MSIX, NuGet packages… |
| 2026-11-14 07:32:31 | [SafeSign.Providers](https://www.nuget.org/packages/SafeSign.Providers) | 1.2.0 | Glenn Watson and Contributors | Signing key providers for SafeSign: Certum SimplySign, cloud KMS and HSM servic… |
| 2026-11-14 07:32:32 | [SafeSign.Signing](https://www.nuget.org/packages/SafeSign.Signing) | 1.2.0 | Glenn Watson and Contributors | Authenticode and CMS signature engine for SafeSign: remote-key signing, RFC 316… |
| 2026-11-14 07:43:55 | [HyperPdfLibrary.Render.Skia](https://www.nuget.org/packages/HyperPdfLibrary.Render.Skia) | 3.7.0 | Glenn Watson | Skia drawing services for HyperPdfLibrary. |
| 2026-11-14 07:43:56 | [HyperPdfLibrary](https://www.nuget.org/packages/HyperPdfLibrary) | 3.7.0 | Glenn Watson | A managed PDF reader, renderer and annotation writer with interchangeable drawi… |
| 2026-11-14 07:46:21 | [Indiko.Geolocation.Library](https://www.nuget.org/packages/Indiko.Geolocation.Library) | 1.0.0 | Indiko | Kerntypen fuer geografische Berechnungen: GeoPoint, Angle, Distance, Dms, Ellip… |
| 2026-11-14 07:46:22 | [Indiko.Geolocation.Library.Astronomy](https://www.nuget.org/packages/Indiko.Geolocation.Library.Astronomy) | 1.0.0 | Indiko | Sonnen- und Mondberechnungen nach Meeus in drei Genauigkeitsstufen: Position, A… |
| 2026-11-14 07:46:23 | [Indiko.Geolocation.Library.Astronomy.Eclipses](https://www.nuget.org/packages/Indiko.Geolocation.Library.Astronomy.Eclipses) | 1.0.0 | Indiko | Sonnen- und Mondfinsternisse aus den Besselschen Elementen des NASA-GSFC-Kanons… |
| 2026-11-14 07:46:24 | [Indiko.Geolocation.Library.Formats](https://www.nuget.org/packages/Indiko.Geolocation.Library.Formats) | 1.0.0 | Indiko | Allokationsfreies Parsen und Formatieren von Koordinaten: Decimal Degree, DDM,… |
| 2026-11-14 07:46:25 | [Indiko.Geolocation.Library.Geodesy](https://www.nuget.org/packages/Indiko.Geolocation.Library.Geodesy) | 1.0.0 | Indiko | Geodaetische Berechnungen auf dem Ellipsoid nach Karney: Entfernung, Peilung, Z… |
| 2026-11-14 07:46:26 | [Indiko.Geolocation.Library.Magnetic](https://www.nuget.org/packages/Indiko.Geolocation.Library.Magnetic) | 1.0.0 | Indiko | Magnetische Deklination, Feldstaerke, Saekularvariation und Unsicherheit nach d… |
| 2026-11-14 07:49:50 | [HowMacro](https://www.nuget.org/packages/HowMacro) | 0.1.2-preview | HowMacro contributors | Compile-time macros for C#. Macros are ordinary C# methods and attributes that… |
| 2026-11-14 07:49:50 | [HowMacro.Testing](https://www.nuget.org/packages/HowMacro.Testing) | 0.1.2-preview | HowMacro contributors | Test helpers for HowMacro macro authors: expand source in a unit test, assert o… |
| 2026-11-14 07:57:07 | [EasySpan](https://www.nuget.org/packages/EasySpan) | 1.0.0 | Ataraxia-Hare | A high-performance collection library based on Span<T>. |
| 2026-11-14 07:58:33 | [Caprine.CronTimer](https://www.nuget.org/packages/Caprine.CronTimer) | 0.1.0 | Caprine Logic | A cron-based alternative to PeriodicTimer with OCPS 1.0 expressions, time zones… |
| 2026-11-14 08:07:13 | [Cratis.Showrunner.Cue](https://www.nuget.org/packages/Cratis.Showrunner.Cue) | 2.10.0 | Cratis | Cue — the Showrunner guided-tour part: remember which guided tours each person… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
