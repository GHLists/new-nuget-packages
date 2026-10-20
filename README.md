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

## Latest list — 2026-10-20 19:22 UTC

New packages created between 2026-10-20 18:22 UTC and 2026-10-20 19:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T19-22-30-414084Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 18:24:01 | [CareJobs](https://www.nuget.org/packages/CareJobs) | 1.0.0 | CareJobs.Now | .NET client for the free CareJobs.Now US healthcare jobs API: search open jobs,… |
| 2026-10-20 18:27:08 | [Sight.Serialization](https://www.nuget.org/packages/Sight.Serialization) | 0.1.0 | Arthur Ferre | Schema-driven binary and text serialization (SBDL format). |
| 2026-10-20 18:28:28 | [Canducci.FileUpload.Mongo](https://www.nuget.org/packages/Canducci.FileUpload.Mongo) | 1.0.0.7 | Fulvio Canducci | MongoDB integration for Canducci.FileUpload. |
| 2026-10-20 18:32:36 | [FocusRgb.PluginSdk](https://www.nuget.org/packages/FocusRgb.PluginSdk) | 1.0.0 | Devantix | Optional .NET process-plugin SDK for the stable FocusRGB 1.x JSON-RPC protocol. |
| 2026-10-20 18:38:08 | [Krafs.Rimworld.Ref.Local](https://www.nuget.org/packages/Krafs.Rimworld.Ref.Local) | 1.0.0 | krafs | Use alongside Krafs.Rimworld.Ref: in Debug builds, compiles your mod against yo… |
| 2026-10-20 18:38:56 | [Trax.StateMachine](https://www.nuget.org/packages/Trax.StateMachine) | 1.68.0 | Theauxm,mark-keaton | Portable, resumable snapshot state-machine engine. Pure: no database or I/O. Re… |
| 2026-10-20 18:38:59 | [Trax.StateMachine.Persistence](https://www.nuget.org/packages/Trax.StateMachine.Persistence) | 1.68.0 | Theauxm,mark-keaton | Persistence for the Trax .NET snapshot state-machine engine: a user-scoped snap… |
| 2026-10-20 18:39:03 | [Trax.StateMachine.Testing](https://www.nuget.org/packages/Trax.StateMachine.Testing) | 1.68.0 | Theauxm,mark-keaton | Cross-runtime differential conformance for Trax .NET state machines: replay a g… |
| 2026-10-20 18:50:13 | [KamuIlanlar.Core.ServiceBus](https://www.nuget.org/packages/KamuIlanlar.Core.ServiceBus) | 1.0.1 | KamuIlanlar.com, Contributors | Transport-independent service bus contracts. |
| 2026-10-20 18:50:14 | [KamuIlanlar.Core.ServiceBus.Wolverine](https://www.nuget.org/packages/KamuIlanlar.Core.ServiceBus.Wolverine) | 1.0.1 | KamuIlanlar.com, Contributors | Wolverine RabbitMQ transport for Core.ServiceBus. |
| 2026-10-20 18:53:46 | [NextLevel.GameStarter](https://www.nuget.org/packages/NextLevel.GameStarter) | 1.0.0 | NextLevel | Everything a NextLevel game backend starts with, behind one AddGameStarter call… |
| 2026-10-20 19:08:03 | [Fickl](https://www.nuget.org/packages/Fickl) | 0.1.0 | Alfonso García-Caro Núñez,Fab… | Fickl: a performance-focused fork of the Fable F# compiler |
| 2026-10-20 19:09:35 | [Plugin.Maui.Spine.AI.Functions](https://www.nuget.org/packages/Plugin.Maui.Spine.AI.Functions) | 0.1.16 | Jonatan Söderberg | Functions the model calls, declared once for a Spine app and its server: where… |
| 2026-10-20 19:09:39 | [Plugin.Maui.Spine.Authentication.Passkeys](https://www.nuget.org/packages/Plugin.Maui.Spine.Authentication.Passkeys) | 0.1.16 | Jonatan Söderberg | Passkeys for Spine sign-in: sign in, sign up and add a passkey to an account th… |
| 2026-10-20 19:09:41 | [Plugin.Maui.Spine.Avatar.Tool](https://www.nuget.org/packages/Plugin.Maui.Spine.Avatar.Tool) | 0.1.16 | Jonatan Söderberg | The spine-avatar command for .spineavatar files: inspect a package, validate it… |
| 2026-10-20 19:09:47 | [Plugin.Maui.Spine.Controls.Avatar](https://www.nuget.org/packages/Plugin.Maui.Spine.Controls.Avatar) | 0.1.16 | Jonatan Söderberg | AvatarView for Spine: animated characters and ambient visuals from .spineavatar… |
| 2026-10-20 19:09:49 | [Plugin.Maui.Spine.Controls.Avatar.Core](https://www.nuget.org/packages/Plugin.Maui.Spine.Controls.Avatar.Core) | 0.1.16 | Jonatan Söderberg | The core of Spine's avatars, without MAUI: the .spineavatar format 1.0 (a safe… |
| 2026-10-20 19:10:09 | [Plugin.Maui.Spine.Speech](https://www.nuget.org/packages/Plugin.Maui.Spine.Speech) | 0.1.16 | Jonatan Söderberg | Text-to-speech for Spine apps with what a caption or an avatar needs to follow… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
