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

## Latest list — 2026-10-14 21:22 UTC

New packages created between 2026-10-14 20:19 UTC and 2026-10-14 21:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T21-22-23-441308Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 20:24:02 | [Lunarium.Common](https://www.nuget.org/packages/Lunarium.Common) | 1.0.0 | Cyanflower | A zero-dependency .NET common library: character-set constants, NanoID and lock… |
| 2026-10-14 20:34:06 | [Shiny.Mobile.CallDirectory](https://www.nuget.org/packages/Shiny.Mobile.CallDirectory) | 6.3.0 | Allan Ritchie | Call blocking and caller identification for .NET - an iOS Call Directory extens… |
| 2026-10-14 20:39:04 | [Ozakboy.Notify.Telegram](https://www.nuget.org/packages/Ozakboy.Notify.Telegram) | 0.1.0 | ozakboy | 建構在 Ozakboy.Http 之上的 Telegram Bot 告警推播,取代 Telegram.Bot:訊息分級(Info / Warning / Cr… |
| 2026-10-14 20:45:53 | [Rldc.Inference.Ollama](https://www.nuget.org/packages/Rldc.Inference.Ollama) | 0.5.0 | Rldc contributors | Ollama chat and System One inference without ONNX runtime dependencies. |
| 2026-10-14 20:49:02 | [PiwiTests.Instrumentation.Coverage](https://www.nuget.org/packages/PiwiTests.Instrumentation.Coverage) | 0.53.0 | piwitests | Per-test server code coverage for Piwi Dashboard: records which code each HTTP… |
| 2026-10-14 20:51:35 | [BorrowedTorch.Audio](https://www.nuget.org/packages/BorrowedTorch.Audio) | 0.9.991 | Vladyslav Pysarenko | Borrowed Torch audio manager |
| 2026-10-14 20:56:40 | [TheBuilder.AppTranslations](https://www.nuget.org/packages/TheBuilder.AppTranslations) | 0.1.0 | Daniel Schmidt | Manage application translation overrides from the Umbraco backoffice. |
| 2026-10-14 21:07:27 | [McpKafka](https://www.nuget.org/packages/McpKafka) | 0.1.0 | matneves | Servidor MCP especialista em Kafka UI (somente leitura): tópicos e mensagens. S… |
| 2026-10-14 21:08:08 | [Tuinet](https://www.nuget.org/packages/Tuinet) | 0.1.0 | Lukasz Maslanka | Performance-first immediate-mode terminal UI library: zero-allocation frames, m… |
| 2026-10-14 21:08:09 | [Tuinet.Testing](https://www.nuget.org/packages/Tuinet.Testing) | 0.1.0 | Lukasz Maslanka | Test helpers for Tuinet apps: styled screen snapshots, a terminal that takes sc… |
| 2026-10-14 21:10:17 | [wordnet](https://www.nuget.org/packages/wordnet) | 1.0.0 | Armen Kirakosyan | Word conversion for .NET: DOC/DOCX exchanges with PDF, Markdown, text, EPUB, MO… |
| 2026-10-14 21:12:07 | [Belin.Which](https://www.nuget.org/packages/Belin.Which) | 2026.10.0 | CedX | Find the instances of an executable in the system path. Like the `which` Linux… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
