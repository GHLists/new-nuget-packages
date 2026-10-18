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

## Latest list — 2026-10-18 22:20 UTC

New packages created between 2026-10-18 21:20 UTC and 2026-10-18 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T22-20-56-425738Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 21:22:40 | [SharpKind.Emulation](https://www.nuget.org/packages/SharpKind.Emulation) | 2.0.0 | Andy Hawkins | Software emulation of the MOS 6502 CPU and the C64 SID sound chip for SharpKind… |
| 2026-10-18 21:22:41 | [SharpKind.Security.Cryptography.Cryptanalysis](https://www.nuget.org/packages/SharpKind.Security.Cryptography.Cryptanalysis) | 2.0.0 | Andy Hawkins | Cryptanalysis of the SharpKind classical ciphers: Caesar by letter frequencies,… |
| 2026-10-18 21:23:41 | [InferenceEngine.ROCm.Runtime.linux-x64](https://www.nuget.org/packages/InferenceEngine.ROCm.Runtime.linux-x64) | 1.24.1.41 | intel-agency | ROCm-accelerated ONNX Runtime native libraries for Linux x64 (AMD GPU) using MI… |
| 2026-10-18 21:30:57 | [XamlVisualEditor.SourceControl.UI](https://www.nuget.org/packages/XamlVisualEditor.SourceControl.UI) | 0.3.0 | Wiesław Šoltés | Source control UI building blocks: unified diff editor, diff lines and data gri… |
| 2026-10-18 21:35:55 | [Pinqponq.Push.Fcm](https://www.nuget.org/packages/Pinqponq.Push.Fcm) | 1.1.0 | Pinqponq | Firebase Cloud Messaging sender: notification and data-only pushes to device to… |
| 2026-10-18 21:37:40 | [Novolis.Game.Sudoku](https://www.nuget.org/packages/Novolis.Game.Sudoku) | 2026.1.1.36 | Novolis | Host-neutral classic Sudoku boards, solving, generation, and difficulty analysi… |
| 2026-10-18 21:38:44 | [Fuaran.UI.Design.Seam](https://www.nuget.org/packages/Fuaran.UI.Design.Seam) | 0.97.0 | Andrew J. Willshire | The design-provider seam of Fuaran UI: the records a design tool and the langua… |
| 2026-10-18 21:49:37 | [Frisket](https://www.nuget.org/packages/Frisket) | 0.1.0 | Frederic Derenty | A document engine with no third-party dependencies: JSON templates and data kep… |
| 2026-10-18 21:49:38 | [Frisket.Import](https://www.nuget.org/packages/Frisket.Import) | 0.1.0 | Frederic Derenty | Reads one page out of an existing PDF and hands it to Frisket, which lays it ou… |
| 2026-10-18 21:49:38 | [Frisket.Fonts](https://www.nuget.org/packages/Frisket.Fonts) | 0.1.0 | Frederic Derenty | The typefaces Frisket draws with when it is given none: Mulish, the default, th… |
| 2026-10-18 21:51:08 | [Bit.BlazeDb.Generators](https://www.nuget.org/packages/Bit.BlazeDb.Generators) | 11.0.0-pre-10 | bit platform | The Roslyn source generator for Bit.BlazeDb: turns [BlazeDbTable] types into ta… |
| 2026-10-18 21:51:10 | [Bit.BlazeDb](https://www.nuget.org/packages/Bit.BlazeDb) | 11.0.0-pre-10 | bit platform | Bit.BlazeDb |
| 2026-10-18 21:51:11 | [Bit.Bsqlite.Storage.IndexedDb](https://www.nuget.org/packages/Bit.Bsqlite.Storage.IndexedDb) | 11.0.0-pre-10 | bit platform | IndexedDB storage for bit Bsqlite, using wa-sqlite's IDBBatchAtomicVFS: persist… |
| 2026-10-18 21:51:13 | [Bit.Bsqlite.Storage.Opfs](https://www.nuget.org/packages/Bit.Bsqlite.Storage.Opfs) | 11.0.0-pre-10 | bit platform | OPFS storage for bit Bsqlite, using wa-sqlite's OPFSCoopSyncVFS: persistent, mu… |
| 2026-10-18 21:51:15 | [Bit.BlazeDb.Browser](https://www.nuget.org/packages/Bit.BlazeDb.Browser) | 11.0.0-pre-10 | bit platform | Bit.BlazeDb.Browser |
| 2026-10-18 21:51:16 | [Bit.Bsqlite.Storage.CacheStorage](https://www.nuget.org/packages/Bit.Bsqlite.Storage.CacheStorage) | 11.0.0-pre-10 | bit platform | Cache Storage for bit Bsqlite: block-based and journal-committed, and the migra… |
| 2026-10-18 22:06:10 | [JRK.JevRunner.Image](https://www.nuget.org/packages/JRK.JevRunner.Image) | 0.5.0-preview-01 | Jeppe Roi Kristensen | Optional SkiaSharp image helpers for JRK.JevRunner. Render normalized Jev bound… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
