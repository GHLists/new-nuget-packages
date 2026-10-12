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

## Latest list — 2026-10-12 08:19 UTC

New packages created between 2026-10-12 07:21 UTC and 2026-10-12 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T08-19-59-134656Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 07:40:38 | [OpenEmail](https://www.nuget.org/packages/OpenEmail) | 0.0.1 | OpenEmail | The official .NET SDK for the OpenEmail API. Send email and broadcasts, work wi… |
| 2026-10-12 07:46:21 | [Xtra.Shared](https://www.nuget.org/packages/Xtra.Shared) | 2.0.2 | Xtra.Shared | Package Description |
| 2026-10-12 07:46:56 | [TheNerdCollective.Integrations.Umbraco.Brevo](https://www.nuget.org/packages/TheNerdCollective.Integrations.Umbraco.Brevo) | 1.0.0 | The Nerd Collective | Brevo backoffice section, dashboard, and CMS settings reader for Umbraco CMS. |
| 2026-10-12 07:55:16 | [Hexabox.Sdk](https://www.nuget.org/packages/Hexabox.Sdk) | 2.10.0 | Massive Dynamic | SDK des extensions .NET de Hexabox : commandes du lanceur HexaLauncher, fenêtre… |
| 2026-10-12 07:55:18 | [Hexabox.Sdk.Ui](https://www.nuget.org/packages/Hexabox.Sdk.Ui) | 2.10.0 | Massive Dynamic | Kit d'interface WinUI des fenêtres d'atelier des extensions Hexabox : contrôles… |
| 2026-10-12 08:05:31 | [GPSR.Core](https://www.nuget.org/packages/GPSR.Core) | 1.0.8-alpha | GPSR.Core | Package Description |
| 2026-10-12 08:05:31 | [GPSR.Utils](https://www.nuget.org/packages/GPSR.Utils) | 1.0.8-alpha | GPSR.Utils | Package Description |
| 2026-10-12 08:05:32 | [GPSR.Data](https://www.nuget.org/packages/GPSR.Data) | 1.0.8-alpha | GPSR.Data | Package Description |
| 2026-10-12 08:05:33 | [GPSR.Runner](https://www.nuget.org/packages/GPSR.Runner) | 1.0.8-alpha | GPSR.Runner | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
