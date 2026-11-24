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

## Latest list — 2026-11-24 01:19 UTC

New packages created between 2026-11-24 00:20 UTC and 2026-11-24 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T01-19-10-009801Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 00:22:50 | [ONI_Together_API](https://www.nuget.org/packages/ONI_Together_API) | 0.8.0 | Lyraedan, Sgt_Imalas | API for third-party mods to add multiplayer features to Oxygen Not Included Tog… |
| 2026-11-24 00:26:01 | [EvilHop](https://www.nuget.org/packages/EvilHop) | 0.4.0 | Suprnova | A .NET library for reading, writing, and manipulating HIP archive files, the bi… |
| 2026-11-24 00:29:37 | [SimpleSign.Adobe.Aatl.Cli](https://www.nuget.org/packages/SimpleSign.Adobe.Aatl.Cli) | 0.16.0 | SimpleSign Contributors | The Adobe Approved Trust List (AATL) for the SimpleSign CLI, installed with 'si… |
| 2026-11-24 00:29:43 | [SimpleSign.Adobe.Aatl](https://www.nuget.org/packages/SimpleSign.Adobe.Aatl) | 0.16.0 | SimpleSign Contributors | Adobe Approved Trust List (AATL) for SimpleSign: the trust anchors Acrobat trus… |
| 2026-11-24 00:32:01 | [ToucanHub.EventStore.ChannelBus](https://www.nuget.org/packages/ToucanHub.EventStore.ChannelBus) | 0.7.0 | junglistkirss | Channel-based EventStore bus |
| 2026-11-24 00:34:59 | [Ahsoka.Extensions.Bluetooth.AudioRouting](https://www.nuget.org/packages/Ahsoka.Extensions.Bluetooth.AudioRouting) | 6.0.1 | Ahsoka.Extensions.Bluetooth.A… | Bluetooth Audio Routing for OpenPV // 60f365e6af3b712659435adb8e2f8c34e4c7c2f5… |
| 2026-11-24 00:35:00 | [Ahsoka.Extensions.Bluetooth.AudioRouting.Client](https://www.nuget.org/packages/Ahsoka.Extensions.Bluetooth.AudioRouting.Client) | 6.0.1 | Ahsoka.Extensions.Bluetooth.A… | OpenPV Bluetooth audio routing service client and contracts. |
| 2026-11-24 00:35:01 | [Ahsoka.Extensions.Bluetooth.Client](https://www.nuget.org/packages/Ahsoka.Extensions.Bluetooth.Client) | 6.0.1 | Ahsoka.Extensions.Bluetooth.C… | OpenPV Bluetooth service clients and contracts. |
| 2026-11-24 00:37:56 | [Ouro.Actions](https://www.nuget.org/packages/Ouro.Actions) | 0.12.1 | Ouro | Ouro UI's action runtime for Windows apps: input validation, idempotency, audit… |
| 2026-11-24 00:37:57 | [Ouro.UI.Windows](https://www.nuget.org/packages/Ouro.UI.Windows) | 0.12.1 | Ouro | Ouro UI for Windows: Button, Badge, Card, Item, Checkbox, Switch, Select, Field… |
| 2026-11-24 00:45:31 | [ScannerSdk](https://www.nuget.org/packages/ScannerSdk) | 2.2.0 | NetumScan | .NET C# wrapper for Scanner SDK C API, with USB CDC preferred on Windows and ma… |
| 2026-11-24 00:45:53 | [EaseFilter.FileControl](https://www.nuget.org/packages/EaseFilter.FileControl) | 5.8.8.1 | EaseFilter | The EaseFilter File Control SDK is a powerful development toolkit designed for… |
| 2026-11-24 00:50:05 | [WinForms.Easel.Generator](https://www.nuget.org/packages/WinForms.Easel.Generator) | 1.0.0 | Axvser | XAML compiler and dependency-property source generators for Easel. |
| 2026-11-24 00:55:56 | [WinForms.Easel](https://www.nuget.org/packages/WinForms.Easel) | 1.0.0 | Axvser | A XAML-first UI runtime for WinForms: dependency properties, a Roslyn XAML comp… |
| 2026-11-24 01:08:13 | [MundoSMS](https://www.nuget.org/packages/MundoSMS) | 1.0.0 | MundoSMS | Cliente de la API REST v3 de MundoSMS (centralita, llamadas, SMS, VozPush, NumC… |
| 2026-11-24 01:12:52 | [Movensys.Login.Core](https://www.nuget.org/packages/Movensys.Login.Core) | 1.1.0 | Movensys Application Team | Created by Movensys Application Team with login timeout, account level, quick l… |
| 2026-11-24 01:13:48 | [Movensys.Login.WinForms](https://www.nuget.org/packages/Movensys.Login.WinForms) | 1.1.0 | Movensys Application Team | Created by Movensys Application Team with login dialog, remain time view and ac… |
| 2026-11-24 01:14:40 | [Movensys.gRPC.Client.WinForms](https://www.nuget.org/packages/Movensys.gRPC.Client.WinForms) | 1.0.21 | Movensys Application Team | Created by Movensys Application Team with gRPC Client GUI functionality |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
