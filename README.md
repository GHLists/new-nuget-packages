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

## Latest list — 2026-10-16 21:21 UTC

New packages created between 2026-10-16 20:20 UTC and 2026-10-16 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T21-21-06-624013Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 20:26:01 | [Fuxion.Tool.Sdk](https://www.nuget.org/packages/Fuxion.Tool.Sdk) | 0.6.1 | Oscar Jimenez | MSBuild SDK of the Fuxion workspace tool (fx): versioning from git, static meta… |
| 2026-10-16 20:42:26 | [RoguelikeToolkit.Entities.Scripting.Jint](https://www.nuget.org/packages/RoguelikeToolkit.Entities.Scripting.Jint) | 6.0.3 | Michael Yarichuk | Jint (JavaScript) scripts for RoguelikeToolkit.Entities templates: pre-parsed,… |
| 2026-10-16 20:43:49 | [FmpReader](https://www.nuget.org/packages/FmpReader) | 0.30.3 | axiom-nz | Read-only .NET reader for FileMaker Pro .fp7 and .fmp12 database files. Lists t… |
| 2026-10-16 21:01:26 | [SimplArchive.Messenger](https://www.nuget.org/packages/SimplArchive.Messenger) | 0.1.0 | Hebel Consulting | The SimplArchive Messenger module: conversations sealed to their members' hardw… |
| 2026-10-16 21:01:27 | [SimplArchive.Messenger.Client](https://www.nuget.org/packages/SimplArchive.Messenger.Client) | 0.2.0 | Hebel Consulting | The SimplArchive Messenger's client library: end-to-end sealed messages and con… |
| 2026-10-16 21:01:28 | [SimplArchive.Messenger.Views](https://www.nuget.org/packages/SimplArchive.Messenger.Views) | 0.1.0 | Hebel Consulting | The SimplArchive Messenger's screens for a cross-platform app: conversations, t… |
| 2026-10-16 21:07:55 | [OneYaml](https://www.nuget.org/packages/OneYaml) | 1.0.0 | Recursive AI, LLC | Pure C# YAML 1.2 that edits a file and keeps its comments, with a System.Text.J… |
| 2026-10-16 21:07:55 | [OneYaml.Compat.SharpYaml](https://www.nuget.org/packages/OneYaml.Compat.SharpYaml) | 1.0.0 | Recursive AI, LLC | A compatibility adapter for code written against the SharpYaml 3 serializer (Ya… |
| 2026-10-16 21:07:56 | [OneYaml.Compat.YamlDotNet](https://www.nuget.org/packages/OneYaml.Compat.YamlDotNet) | 1.0.0 | Recursive AI, LLC | A compatibility adapter for code written against YamlDotNet 18 (serializer buil… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
