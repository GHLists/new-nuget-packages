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

## Latest list — 2026-10-29 14:19 UTC

New packages created between 2026-10-29 13:21 UTC and 2026-10-29 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T14-19-33-357176Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 13:33:31 | [Naratteu.Anonymous](https://www.nuget.org/packages/Naratteu.Anonymous) | 0.1.0 | naratteu | 인터페이스를 자바 익명클래스처럼 그 자리에서 구현하게 해주는 소스제너레이터 |
| 2026-10-29 13:41:11 | [Scarlet.System.Text.Json.IgnoreCondition](https://www.nuget.org/packages/Scarlet.System.Text.Json.IgnoreCondition) | 1.0.0 | ScarletKuro | Adds WhenReadingNull and WhenReadingDefault to System.Text.Json alongside nativ… |
| 2026-10-29 13:42:34 | [Simorgh.AI.Routing](https://www.nuget.org/packages/Simorgh.AI.Routing) | 0.1.4 | Simorgh AI Contributors | Extensible model routing for Simorgh.AI. |
| 2026-10-29 13:52:55 | [ChzzkApi-CS](https://www.nuget.org/packages/ChzzkApi-CS) | 1.0.0 | Null38 | Chzzk Open API C# client library |
| 2026-10-29 13:58:03 | [Beckhoff.TwinCAT.HMI.OAuth](https://www.nuget.org/packages/Beckhoff.TwinCAT.HMI.OAuth) | 25.0.122 | Beckhoff | TwinCAT HMI is a development environment for web-based HMIs (Human Machine Inte… |
| 2026-10-29 14:09:41 | [Amber.Audio.OpenAL](https://www.nuget.org/packages/Amber.Audio.OpenAL) | 0.1.0 | Robert Schneckenhaus | OpenAL implementation of the Amber audio interfaces. |
| 2026-10-29 14:09:42 | [Amber.Renderer.OpenGL](https://www.nuget.org/packages/Amber.Renderer.OpenGL) | 0.1.0 | Robert Schneckenhaus | OpenGL implementation of the Amber renderer interfaces. |
| 2026-10-29 14:09:44 | [Amber.Common](https://www.nuget.org/packages/Amber.Common) | 0.1.0 | Robert Schneckenhaus | Basic utilities which all other Amber projects might use. |
| 2026-10-29 14:09:45 | [Amber.Assets.Common](https://www.nuget.org/packages/Amber.Assets.Common) | 0.1.0 | Robert Schneckenhaus | Interfaces and general classes for working with assets. |
| 2026-10-29 14:09:45 | [Amber.IO.FileSystem](https://www.nuget.org/packages/Amber.IO.FileSystem) | 0.1.0 | Robert Schneckenhaus | Implementation of different file systems (e.g. virtual and operating system). |
| 2026-10-29 14:09:47 | [Amber.IO.FileFormats](https://www.nuget.org/packages/Amber.IO.FileFormats) | 0.1.0 | Robert Schneckenhaus | Common file formats used in Amberstar and Ambermoon like the container files, w… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
