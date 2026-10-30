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

## Latest list — 2026-10-30 05:21 UTC

New packages created between 2026-10-30 04:20 UTC and 2026-10-30 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T05-21-36-264457Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 04:33:43 | [Innovayse.SDK](https://www.nuget.org/packages/Innovayse.SDK) | 1.2.0 | Hostpanel contributors | Plugin contracts for hostpanel: provisioning, payment, registrar, identity, ful… |
| 2026-10-30 04:49:10 | [PowerPointCompareForGit](https://www.nuget.org/packages/PowerPointCompareForGit) | 0.1.1 | Llewellyn Falco | Render PowerPoint decks from git history to PNG and compare versions in your di… |
| 2026-10-30 04:55:01 | [Bitbeans.Zpl.Viewer](https://www.nuget.org/packages/Bitbeans.Zpl.Viewer) | 1.0.0 | bitbeans | Render ZPL II labels to PNG/JPEG with SkiaSharp, an offline alternative to labe… |
| 2026-10-30 04:55:02 | [Bitbeans.Zpl.SkiaSharp](https://www.nuget.org/packages/Bitbeans.Zpl.SkiaSharp) | 1.0.0 | bitbeans | SkiaSharp based image conversion for Bitbeans.Zpl (~DG and ~DY graphics, GRF to… |
| 2026-10-30 04:55:02 | [Bitbeans.Zpl](https://www.nuget.org/packages/Bitbeans.Zpl) | 1.0.0 | bitbeans | Create Zebra ZPL II labels with strongly typed elements. Dependency-free: image… |
| 2026-10-30 04:56:12 | [Superroute.SPrint](https://www.nuget.org/packages/Superroute.SPrint) | 0.1.0 | Superroute | sPrint, Superroute's printing SDK for .NET: find network, USB and Bluetooth pri… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
