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

## Latest list — 2026-10-10 23:19 UTC

New packages created between 2026-10-10 22:20 UTC and 2026-10-10 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T23-19-09-722124Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 22:27:37 | [NativeValidation](https://www.nuget.org/packages/NativeValidation) | 0.1.0 | Daniel Cazzulino | AOT-safe validation for System.ComponentModel.DataAnnotations attributes. |
| 2026-10-10 22:27:55 | [WizardKit](https://www.nuget.org/packages/WizardKit) | 1.0.1 | Thomas Loeb | A reusable Windows Forms installation-wizard control (TabControl-style multi-st… |
| 2026-10-10 22:28:07 | [WizardKit.Templates](https://www.nuget.org/packages/WizardKit.Templates) | 1.0.1 | Thomas Loeb | Reusable, front-end-only wizard pages for WizardKit. Consumers instantiate a pa… |
| 2026-10-10 23:01:48 | [PlatformHeads](https://www.nuget.org/packages/PlatformHeads) | 0.1.0 | https://github.com/SimonCropp… | The build and packaging half of an app with one head per platform: publishes a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
