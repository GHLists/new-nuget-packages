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

## Latest list — 2026-11-18 14:21 UTC

New packages created between 2026-11-18 13:21 UTC and 2026-11-18 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T14-21-48-230638Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 13:22:12 | [AcceleratedKAZE](https://www.nuget.org/packages/AcceleratedKAZE) | 0.0.1-beta | Cularr | A managed .NET implementation of the AKAZE feature detector and the TEBLID desc… |
| 2026-11-18 13:35:23 | [Asteroid.PushProbe](https://www.nuget.org/packages/Asteroid.PushProbe) | 0.0.2 | probe | temporary push probe |
| 2026-11-18 13:36:21 | [Pulumi.Labs.Openai](https://www.nuget.org/packages/Pulumi.Labs.Openai) | 0.2.0 | Pulumi Labs | A Pulumi provider for managing resources in OpenAI. |
| 2026-11-18 13:40:49 | [DOtrishko.LiteSettings](https://www.nuget.org/packages/DOtrishko.LiteSettings) | 1.0.0 | Dmytro Otrishko | Lightweight settings library for .NET. Mark properties with [Save] and persist… |
| 2026-11-18 13:41:11 | [DOtrishko.LiteSettings.Xml](https://www.nuget.org/packages/DOtrishko.LiteSettings.Xml) | 1.0.0 | Dmytro Otrishko | XML format for LiteSettings. Stores [Save] properties in settings.xml under the… |
| 2026-11-18 13:55:31 | [Validex](https://www.nuget.org/packages/Validex) | 1.0.0 | YourName | A lightweight and extensible .NET validation library. |
| 2026-11-18 14:04:46 | [Ekom.Payments.Stripe](https://www.nuget.org/packages/Ekom.Payments.Stripe) | 1.1.1 | Vettvangur | Ekom Payments Stripe - Vettvangur E-Commerce solution |
| 2026-11-18 14:05:24 | [AidDev.Ricochet](https://www.nuget.org/packages/AidDev.Ricochet) | 0.0.1 | OJ | Black-box integration testing for HTTP JSON/REST APIs: lay out steps as a plan… |
| 2026-11-18 14:05:25 | [AidDev.Ricochet.Console](https://www.nuget.org/packages/AidDev.Ricochet.Console) | 0.0.1 | OJ | Console front end for Ricochet: a Spectre.Console reporter (streamed failures,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
