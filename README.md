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

## Latest list — 2026-10-22 08:21 UTC

New packages created between 2026-10-22 07:20 UTC and 2026-10-22 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T08-21-41-521585Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 07:30:00 | [RavenDB.Zstd.Native](https://www.nuget.org/packages/RavenDB.Zstd.Native) | 1.5.7 | RavenDB | Native libzstd v1.5.7 (https://github.com/facebook/zstd) for win-x86, win-x64,… |
| 2026-10-22 07:33:57 | [Envisia.EmbeddedNodeJs26.Native.linux-arm64](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26.Native.linux-arm64) | 0.6.0 | Embedded NodeJS | Embedded Node.js runtime for linux-arm64. |
| 2026-10-22 07:33:57 | [Envisia.EmbeddedNodeJs26](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26) | 0.6.0 | Embedded NodeJS | Embeds prebuilt Node.js binaries (win/linux/mac, x64/arm64) for use by JavaScri… |
| 2026-10-22 07:33:59 | [Envisia.EmbeddedNodeJs26.Native.win-x64](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26.Native.win-x64) | 0.6.0 | Embedded NodeJS | Embedded Node.js runtime for win-x64. |
| 2026-10-22 07:34:01 | [Envisia.EmbeddedNodeJs26.Native.win-arm64](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26.Native.win-arm64) | 0.6.0 | Embedded NodeJS | Embedded Node.js runtime for win-arm64. |
| 2026-10-22 07:34:03 | [Envisia.EmbeddedNodeJs26.Native.osx-x64](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26.Native.osx-x64) | 0.6.0 | Embedded NodeJS | Embedded Node.js runtime for osx-x64. |
| 2026-10-22 07:34:06 | [Envisia.EmbeddedNodeJs26.Native.osx-arm64](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26.Native.osx-arm64) | 0.6.0 | Embedded NodeJS | Embedded Node.js runtime for osx-arm64. |
| 2026-10-22 07:34:08 | [Envisia.EmbeddedNodeJs26.Native.linux-x64](https://www.nuget.org/packages/Envisia.EmbeddedNodeJs26.Native.linux-x64) | 0.6.0 | Embedded NodeJS | Embedded Node.js runtime for linux-x64. |
| 2026-10-22 07:53:43 | [RustNetRuntime](https://www.nuget.org/packages/RustNetRuntime) | 0.1.0 | Gravicode Studios | RustNetRuntime: a .NET runtime (RustCLR) written in Rust. The rustnet command b… |
| 2026-10-22 07:54:29 | [Webority.Jobs](https://www.nuget.org/packages/Webority.Jobs) | 0.27.0 | Webority.Jobs | DestructiveRunGuard: one brake for scheduled jobs that delete data or remove ac… |
| 2026-10-22 07:58:55 | [FS.GG.SDD.Commands](https://www.nuget.org/packages/FS.GG.SDD.Commands) | 2.3.0 | FS.GG | Native lifecycle command workflow contracts for FS.GG.SDD. |
| 2026-10-22 07:59:44 | [Hosihikari.Testing](https://www.nuget.org/packages/Hosihikari.Testing) | 1.0.0 | HosihikariFramework | Test host and in-memory host services for Hosihikari plugins. |
| 2026-10-22 07:59:44 | [Hosihikari.Plugin.Build](https://www.nuget.org/packages/Hosihikari.Plugin.Build) | 1.0.0 | HosihikariFramework | MSBuild PackPlugin target for Hosihikari plugin packages. |
| 2026-10-22 08:03:24 | [mdu](https://www.nuget.org/packages/mdu) | 5.0.0 | Jan Ruhlaender | MDU (Markdown Documentation Utility) for linting and rendering Markdown documen… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
