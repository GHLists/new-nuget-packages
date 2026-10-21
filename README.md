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

## Latest list — 2026-10-21 15:20 UTC

New packages created between 2026-10-21 14:22 UTC and 2026-10-21 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T15-20-10-498287Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 14:28:57 | [Asgard.Loki.Abstractions](https://www.nuget.org/packages/Asgard.Loki.Abstractions) | 1.0.0 | BenLampson | Generic client and module extension contracts for Asgard.Loki. |
| 2026-10-21 14:28:58 | [Asgard.Loki.Infrastructure](https://www.nuget.org/packages/Asgard.Loki.Infrastructure) | 1.0.0 | BenLampson | Capability-independent transport primitives for Asgard.Loki providers. |
| 2026-10-21 14:28:59 | [Asgard.Loki](https://www.nuget.org/packages/Asgard.Loki) | 1.0.0 | BenLampson | Unified client implementation and module lifecycle for Asgard.Loki. |
| 2026-10-21 14:29:00 | [Asgard.Loki.LLM](https://www.nuget.org/packages/Asgard.Loki.LLM) | 1.0.0 | BenLampson | LLM contracts, model routing and shared Session bindings for Asgard.Loki. |
| 2026-10-21 14:29:01 | [Asgard.Loki.Audio](https://www.nuget.org/packages/Asgard.Loki.Audio) | 1.0.0 | BenLampson | Independent audio capability for Asgard.Loki. |
| 2026-10-21 14:29:02 | [Asgard.Loki.Image](https://www.nuget.org/packages/Asgard.Loki.Image) | 1.0.0 | BenLampson | Independent image generation and editing contracts and module for Asgard.Loki. |
| 2026-10-21 14:29:03 | [Asgard.Loki.Embedding](https://www.nuget.org/packages/Asgard.Loki.Embedding) | 1.0.0 | BenLampson | Independent native embedding contracts and module for Asgard.Loki. |
| 2026-10-21 14:29:04 | [Asgard.Loki.Rerank](https://www.nuget.org/packages/Asgard.Loki.Rerank) | 1.0.0 | BenLampson | Independent native rerank contracts and module for Asgard.Loki. |
| 2026-10-21 14:29:05 | [Asgard.Loki.Video](https://www.nuget.org/packages/Asgard.Loki.Video) | 1.0.0 | BenLampson | Independent native video task calls and complete-target task binding for Asgard… |
| 2026-10-21 14:29:06 | [Asgard.Loki.LLM.Volcengine](https://www.nuget.org/packages/Asgard.Loki.LLM.Volcengine) | 1.0.0 | BenLampson | Volcengine Ark LLM provider for Asgard.Loki. |
| 2026-10-21 14:29:07 | [Asgard.Loki.LLM.OpenAI](https://www.nuget.org/packages/Asgard.Loki.LLM.OpenAI) | 1.0.0 | BenLampson | OpenAI Chat Completions and Responses provider for Asgard.Loki. |
| 2026-10-21 14:29:08 | [Asgard.Loki.LLM.Anthropic](https://www.nuget.org/packages/Asgard.Loki.LLM.Anthropic) | 1.0.0 | BenLampson | Anthropic Claude Messages native provider for Asgard.Loki. |
| 2026-10-21 14:29:09 | [Asgard.Loki.LLM.Google](https://www.nuget.org/packages/Asgard.Loki.LLM.Google) | 1.0.0 | BenLampson | Google Gemini generateContent native provider for Asgard.Loki. |
| 2026-10-21 14:29:10 | [Asgard.Loki.LLM.Ollama](https://www.nuget.org/packages/Asgard.Loki.LLM.Ollama) | 1.0.0 | BenLampson | Native Ollama chat/generate JSON and NDJSON provider for Asgard.Loki. |
| 2026-10-21 14:29:11 | [Asgard.Loki.LLM.Azure](https://www.nuget.org/packages/Asgard.Loki.LLM.Azure) | 1.0.0 | BenLampson | Native Azure OpenAI model calls with explicit API routing and borrowed external… |
| 2026-10-21 14:29:12 | [Asgard.Loki.LLM.GoogleVertex](https://www.nuget.org/packages/Asgard.Loki.LLM.GoogleVertex) | 1.0.0 | BenLampson | Native Vertex Gemini, Claude and MaaS Chat calls with explicit target identity… |
| 2026-10-21 14:29:16 | [Asgard.Loki.LLM.AWS](https://www.nuget.org/packages/Asgard.Loki.LLM.AWS) | 1.0.0 | BenLampson | Native Bedrock Claude and Converse calls with explicit targets, borrowed SigV4… |
| 2026-10-21 14:29:17 | [Asgard.Loki.LLM.Cloudflare](https://www.nuget.org/packages/Asgard.Loki.LLM.Cloudflare) | 1.0.0 | BenLampson | Native Workers AI ai/run text JSON and SSE provider for Asgard.Loki. |
| 2026-10-21 14:29:18 | [Asgard.Loki.LLM.Cohere](https://www.nuget.org/packages/Asgard.Loki.LLM.Cohere) | 1.0.0 | BenLampson | Native Cohere v1 Chat JSON and NDJSON provider for Asgard.Loki. |
| 2026-10-21 14:29:19 | [Asgard.Loki.LLM.Coze](https://www.nuget.org/packages/Asgard.Loki.LLM.Coze) | 1.0.0 | BenLampson | Explicit native Coze v3 bot chat calls for Asgard.Loki without polling or model… |
| 2026-10-21 14:29:20 | [Asgard.Loki.LLM.DeepSeek](https://www.nuget.org/packages/Asgard.Loki.LLM.DeepSeek) | 1.0.0 | BenLampson | Native DeepSeek Search and Fetch JSON calls with explicitly fixed service crede… |
| 2026-10-21 14:29:21 | [Asgard.Loki.LLM.Dify](https://www.nuget.org/packages/Asgard.Loki.LLM.Dify) | 1.0.0 | BenLampson | Explicit native Dify app chat JSON/SSE without model projection, workflow hosti… |
| 2026-10-21 14:29:22 | [Asgard.Loki.LLM.MiniMax](https://www.nuget.org/packages/Asgard.Loki.LLM.MiniMax) | 1.0.0 | BenLampson | Native MiniMax v2 Chat JSON and SSE provider for Asgard.Loki. |
| 2026-10-21 14:29:23 | [Asgard.Loki.LLM.NewAPI](https://www.nuget.org/packages/Asgard.Loki.LLM.NewAPI) | 1.0.0 | BenLampson | Explicit API-Key native alpha/search client for existing New API and Sub2API up… |
| 2026-10-21 14:29:24 | [Asgard.Loki.LLM.Perplexity](https://www.nuget.org/packages/Asgard.Loki.LLM.Perplexity) | 1.0.0 | BenLampson | Native Perplexity Responses and Sonar Chat JSON and SSE providers for Asgard.Lo… |
| 2026-10-21 14:29:25 | [Asgard.Loki.LLM.Tencent](https://www.nuget.org/packages/Asgard.Loki.LLM.Tencent) | 1.0.0 | BenLampson | Native Tencent Hunyuan model calls with supplier-local TC3 authentication. |
| 2026-10-21 14:29:26 | [Asgard.Loki.LLM.Xunfei](https://www.nuget.org/packages/Asgard.Loki.LLM.Xunfei) | 1.0.0 | BenLampson | Native Xunfei Spark WebSocket model calls with explicit signed targets and immu… |
| 2026-10-21 14:29:27 | [Asgard.Loki.LLM.Conversion](https://www.nuget.org/packages/Asgard.Loki.LLM.Conversion) | 1.0.0 | BenLampson | Explicit, diagnostic LLM protocol conversion for Asgard.Loki. |
| 2026-10-21 14:29:28 | [Asgard.Loki.Audio.Volcengine](https://www.nuget.org/packages/Asgard.Loki.Audio.Volcengine) | 1.0.0 | BenLampson | Volcengine V3 HTTP and explicit V1 native speech synthesis provider for Asgard.… |
| 2026-10-21 14:29:29 | [Asgard.Loki.Video.Volcengine](https://www.nuget.org/packages/Asgard.Loki.Video.Volcengine) | 1.0.0 | BenLampson | Native Volcengine Ark video task provider for Asgard.Loki. |
| 2026-10-21 14:29:30 | [Asgard.Loki.Video.Ali](https://www.nuget.org/packages/Asgard.Loki.Video.Ali) | 1.0.0 | BenLampson | Native Alibaba Cloud DashScope video task provider for Asgard.Loki. |
| 2026-10-21 14:29:31 | [Asgard.Loki.Video.Google](https://www.nuget.org/packages/Asgard.Loki.Video.Google) | 1.0.0 | BenLampson | Native Gemini Developer API Veo video task provider for Asgard.Loki. |
| 2026-10-21 14:29:32 | [Asgard.Loki.Video.GoogleVertex](https://www.nuget.org/packages/Asgard.Loki.Video.GoogleVertex) | 1.0.0 | BenLampson | Native resource-scoped Vertex Veo video provider for Asgard.Loki. |
| 2026-10-21 14:29:33 | [Asgard.Loki.Video.MiniMax](https://www.nuget.org/packages/Asgard.Loki.Video.MiniMax) | 1.0.0 | BenLampson | Native MiniMax video v1/v2 task provider for Asgard.Loki. |
| 2026-10-21 14:29:34 | [Asgard.Loki.Video.Kling](https://www.nuget.org/packages/Asgard.Loki.Video.Kling) | 1.0.0 | BenLampson | Native Kling text2video/image2video task provider for Asgard.Loki. |
| 2026-10-21 14:29:35 | [Asgard.Loki.Video.Vidu](https://www.nuget.org/packages/Asgard.Loki.Video.Vidu) | 1.0.0 | BenLampson | Native Vidu video generation and task-query provider for Asgard.Loki. |
| 2026-10-21 14:29:36 | [Asgard.Loki.Video.XAI](https://www.nuget.org/packages/Asgard.Loki.Video.XAI) | 1.0.0 | BenLampson | Native xAI video generation, editing, extension and task-query provider for Asg… |
| 2026-10-21 14:29:37 | [Asgard.Loki.Video.Midjourney](https://www.nuget.org/packages/Asgard.Loki.Video.Midjourney) | 1.0.0 | BenLampson | Native unofficial Midjourney proxy video calls for Asgard.Loki. |
| 2026-10-21 14:29:38 | [Asgard.Loki.Audio.OpenAI](https://www.nuget.org/packages/Asgard.Loki.Audio.OpenAI) | 1.0.0 | BenLampson | Native OpenAI speech, file transcription and translation provider for Asgard.Lo… |
| 2026-10-21 14:29:39 | [Asgard.Loki.Audio.MiniMax](https://www.nuget.org/packages/Asgard.Loki.Audio.MiniMax) | 1.0.0 | BenLampson | Native MiniMax synchronous HTTP speech synthesis provider for Asgard.Loki. |
| 2026-10-21 14:29:40 | [Asgard.Loki.Audio.Cloudflare](https://www.nuget.org/packages/Asgard.Loki.Audio.Cloudflare) | 1.0.0 | BenLampson | Explicit native Cloudflare Workers AI audio recognition and translation provide… |
| 2026-10-21 14:29:41 | [Asgard.Loki.Audio.Azure](https://www.nuget.org/packages/Asgard.Loki.Audio.Azure) | 1.0.0 | BenLampson | Native deployment-scoped Azure audio speech, transcription and translation prov… |
| 2026-10-21 14:29:42 | [Asgard.Loki.Audio.SunoAPI](https://www.nuget.org/packages/Asgard.Loki.Audio.SunoAPI) | 1.0.0 | BenLampson | Explicit native Suno-API music and lyrics task calls for Asgard.Loki. |
| 2026-10-21 14:29:43 | [Asgard.Loki.Image.OpenAI](https://www.nuget.org/packages/Asgard.Loki.Image.OpenAI) | 1.0.0 | BenLampson | OpenAI image generation and editing provider for Asgard.Loki. |
| 2026-10-21 14:29:44 | [Asgard.Loki.Image.Azure](https://www.nuget.org/packages/Asgard.Loki.Image.Azure) | 1.0.0 | BenLampson | Native deployment-scoped Azure image generation and multipart editing for Asgar… |
| 2026-10-21 14:29:45 | [Asgard.Loki.Image.Midjourney](https://www.nuget.org/packages/Asgard.Loki.Image.Midjourney) | 1.0.0 | BenLampson | Explicit native Midjourney proxy image operations and original task outcomes fo… |
| 2026-10-21 14:29:46 | [Asgard.Loki.Image.Replicate](https://www.nuget.org/packages/Asgard.Loki.Image.Replicate) | 1.0.0 | BenLampson | Native Replicate model image predictions and explicit model-input upload for As… |
| 2026-10-21 14:29:47 | [Asgard.Loki.Image.Zhipu](https://www.nuget.org/packages/Asgard.Loki.Image.Zhipu) | 1.0.0 | BenLampson | Native Zhipu v4 image generation with original image carriers, content filterin… |
| 2026-10-21 14:29:48 | [Asgard.Loki.Image.XAI](https://www.nuget.org/packages/Asgard.Loki.Image.XAI) | 1.0.0 | BenLampson | Native xAI JSON image editing with original ordered image references and comple… |
| 2026-10-21 14:29:49 | [Asgard.Loki.Image.SiliconFlow](https://www.nuget.org/packages/Asgard.Loki.Image.SiliconFlow) | 1.0.0 | BenLampson | Native SiliconFlow image generation with original images, timings and seed for… |
| 2026-10-21 14:29:50 | [Asgard.Loki.Image.MiniMax](https://www.nuget.org/packages/Asgard.Loki.Image.MiniMax) | 1.0.0 | BenLampson | Native MiniMax image generation and subject references with original URL/Base64… |
| 2026-10-21 14:29:52 | [Asgard.Loki.Image.GoogleVertex](https://www.nuget.org/packages/Asgard.Loki.Image.GoogleVertex) | 1.0.0 | BenLampson | Native resource-scoped Vertex Gemini images with explicit Bearer or API-Key aut… |
| 2026-10-21 14:29:53 | [Asgard.Loki.Image.Google](https://www.nuget.org/packages/Asgard.Loki.Image.Google) | 1.0.0 | BenLampson | Native Gemini image generation, editing inputs and original safety-aware SSE fo… |
| 2026-10-21 14:29:54 | [Asgard.Loki.Image.Ali](https://www.nuget.org/packages/Asgard.Loki.Image.Ali) | 1.0.0 | BenLampson | Native Ali image JSON, interleaved SSE and caller-driven image tasks for Asgard… |
| 2026-10-21 14:29:55 | [Asgard.Loki.Image.Volcengine](https://www.nuget.org/packages/Asgard.Loki.Image.Volcengine) | 1.0.0 | BenLampson | Native Ark JSON/SSE and independently signed Jimeng Visual image generation for… |
| 2026-10-21 14:29:56 | [Asgard.Loki.Embedding.Azure](https://www.nuget.org/packages/Asgard.Loki.Embedding.Azure) | 1.0.0 | BenLampson | Native deployment-scoped Azure embeddings with explicit API version and origina… |
| 2026-10-21 14:29:57 | [Asgard.Loki.Embedding.OpenAI](https://www.nuget.org/packages/Asgard.Loki.Embedding.OpenAI) | 1.0.0 | BenLampson | Native OpenAI embeddings provider for Asgard.Loki. |
| 2026-10-21 14:29:58 | [Asgard.Loki.Embedding.Google](https://www.nuget.org/packages/Asgard.Loki.Embedding.Google) | 1.0.0 | BenLampson | Native Google Gemini embedding provider for Asgard.Loki. |
| 2026-10-21 14:29:59 | [Asgard.Loki.Embedding.Ollama](https://www.nuget.org/packages/Asgard.Loki.Embedding.Ollama) | 1.0.0 | BenLampson | Native Ollama embedding provider for Asgard.Loki. |
| 2026-10-21 14:30:00 | [Asgard.Loki.Embedding.Jina](https://www.nuget.org/packages/Asgard.Loki.Embedding.Jina) | 1.0.0 | BenLampson | Native Jina dense and multi-vector embedding provider for Asgard.Loki. |
| 2026-10-21 14:30:01 | [Asgard.Loki.Rerank.Cohere](https://www.nuget.org/packages/Asgard.Loki.Rerank.Cohere) | 1.0.0 | BenLampson | Native Cohere v1/v2 reranking provider for Asgard.Loki. |
| 2026-10-21 14:30:02 | [Asgard.Loki.Rerank.Jina](https://www.nuget.org/packages/Asgard.Loki.Rerank.Jina) | 1.0.0 | BenLampson | Native Jina text and multimodal reranking provider for Asgard.Loki. |
| 2026-10-21 14:30:03 | [Asgard.Loki.Rerank.Ali](https://www.nuget.org/packages/Asgard.Loki.Rerank.Ali) | 1.0.0 | BenLampson | Native Alibaba Cloud DashScope rerank provider for Asgard.Loki. |
| 2026-10-21 14:30:04 | [Asgard.Loki.Rerank.SiliconFlow](https://www.nuget.org/packages/Asgard.Loki.Rerank.SiliconFlow) | 1.0.0 | BenLampson | Native SiliconFlow text and image reranking provider for Asgard.Loki. |
| 2026-10-21 14:30:05 | [Asgard.Loki.Rerank.OpenAICompatible](https://www.nuget.org/packages/Asgard.Loki.Rerank.OpenAICompatible) | 1.0.0 | BenLampson | Explicit native OpenAI-compatible rerank wire for Asgard.Loki. |
| 2026-10-21 14:30:06 | [Asgard.Loki.Rerank.SGLang](https://www.nuget.org/packages/Asgard.Loki.Rerank.SGLang) | 1.0.0 | BenLampson | Native SGLang reranking with original score arrays for Asgard.Loki. |
| 2026-10-21 14:40:27 | [ahmedhakamidev](https://www.nuget.org/packages/ahmedhakamidev) | 1.0.0 | Ahmed Hakami | A reserved NuGet package for Ahmed Hakami |
| 2026-10-21 14:55:25 | [CanFx.Realtime.SignalR](https://www.nuget.org/packages/CanFx.Realtime.SignalR) | 0.1.0 | Oğuzhan Can | IRealtimeNotifier'ın SignalR implementasyonu: kimliği doğrulanmış bağlantıları… |
| 2026-10-21 14:55:25 | [CanFx.Search.Elasticsearch](https://www.nuget.org/packages/CanFx.Search.Elasticsearch) | 0.1.0 | Oğuzhan Can | Elasticsearch / OpenSearch arama motoru (ISearchEngine). Resmî istemci yerine H… |
| 2026-10-21 14:55:26 | [CanFx.Settings.AspNetCore](https://www.nuget.org/packages/CanFx.Settings.AspNetCore) | 0.1.0 | Oğuzhan Can | Ayarların yönetim uç noktaları (listele, değiştir, sıfırla, istemci değerleri;… |
| 2026-10-21 14:55:26 | [CanFx.Localization](https://www.nuget.org/packages/CanFx.Localization) | 0.1.0 | Oğuzhan Can | JSON dosyalarından okuyan IStringLocalizer (resx gerekmez): kültür zinciri (tr-… |
| 2026-10-21 14:55:27 | [CanFx.Testing](https://www.nuget.org/packages/CanFx.Testing) | 0.1.0 | Oğuzhan Can | CanFx ile yazılan uygulamaların testleri için: elle ilerletilen saat (zamanlayı… |
| 2026-10-21 14:55:28 | [CanFx.Redis.ScaleOut](https://www.nuget.org/packages/CanFx.Redis.ScaleOut) | 0.1.0 | Oğuzhan Can | Uygulamayı birden çok sunucuda çalıştırmak için Redis: ortak Data Protection an… |
| 2026-10-21 14:55:28 | [CanFx.Domain](https://www.nuget.org/packages/CanFx.Domain) | 0.1.0 | Oğuzhan Can | DDD yapı taşları: Entity, AggregateRoot, ValueObject, domain event'ler ve audit… |
| 2026-10-21 14:55:29 | [CanFx.Observability.OpenTelemetry](https://www.nuget.org/packages/CanFx.Observability.OpenTelemetry) | 0.1.0 | Oğuzhan Can | CanFx paketlerinin ve .NET'in yerleşik telemetrisini (ASP.NET Core, HttpClient,… |
| 2026-10-21 14:55:30 | [CanFx.Persistence](https://www.nuget.org/packages/CanFx.Persistence) | 0.1.0 | Oğuzhan Can | EF Core implementasyonu: CanDbContext (soft delete + tenant filtreleri), EfRepo… |
| 2026-10-21 14:55:30 | [CanFx.Persistence.Abstractions](https://www.nuget.org/packages/CanFx.Persistence.Abstractions) | 0.1.0 | Oğuzhan Can | Repository, Unit of Work, dinamik filtreleme/sıralama ve sayfalama sözleşmeleri… |
| 2026-10-21 14:55:31 | [CanFx.FileStorage](https://www.nuget.org/packages/CanFx.FileStorage) | 0.1.0 | Oğuzhan Can | Dosya depolama soyutlaması (IFileStorage), yerel disk implementasyonu ve tenant… |
| 2026-10-21 14:55:31 | [CanFx.Reporting.EntityFrameworkCore](https://www.nuget.org/packages/CanFx.Reporting.EntityFrameworkCore) | 0.1.0 | Oğuzhan Can | Kaydedilmiş raporlar için EF Core deposu ve tablo yapılandırması (SavedReports). |
| 2026-10-21 14:55:32 | [CanFx.EventBus.Kafka](https://www.nuget.org/packages/CanFx.EventBus.Kafka) | 0.1.0 | Oğuzhan Can | CanFx.EventBus için Apache Kafka taşıyıcısı: event başına topic, idempotent pro… |
| 2026-10-21 14:55:33 | [CanFx.Mediator.Abstractions](https://www.nuget.org/packages/CanFx.Mediator.Abstractions) | 0.1.0 | Oğuzhan Can | CanFx.Mediator arayüzleri: IRequest, IRequestHandler, INotificationHandler, IPi… |
| 2026-10-21 14:55:33 | [CanFx.Mailing.SendGrid](https://www.nuget.org/packages/CanFx.Mailing.SendGrid) | 0.1.0 | Oğuzhan Can | IEmailSender'ın SendGrid (Web API v3) implementasyonu. SendGrid SDK'sı yerine d… |
| 2026-10-21 14:55:34 | [CanFx.BackgroundJobs.Hangfire](https://www.nuget.org/packages/CanFx.BackgroundJobs.Hangfire) | 0.1.0 | Oğuzhan Can | IBackgroundJobQueue'yu Hangfire'a bağlar: kalıcı kuyruk, otomatik yeniden denem… |
| 2026-10-21 14:55:35 | [CanFx.BackgroundJobs](https://www.nuget.org/packages/CanFx.BackgroundJobs) | 0.1.0 | Oğuzhan Can | Arka plan işleri: tenant'ı koruyan kuyruk (fire-and-forget) ve belirli aralıkla… |
| 2026-10-21 14:55:35 | [CanFx.Reporting](https://www.nuget.org/packages/CanFx.Reporting) | 0.1.0 | Oğuzhan Can | Raporlama ve istatistik motoru: pivot (satır/sütun gruplama, ara ve genel topla… |
| 2026-10-21 14:55:36 | [CanFx.FileStorage.AzureBlob](https://www.nuget.org/packages/CanFx.FileStorage.AzureBlob) | 0.1.0 | Oğuzhan Can | Azure Blob Storage (ve Azurite) için IFileStorage. Azure SDK'sı yerine HttpClie… |
| 2026-10-21 14:55:37 | [CanFx.Mapping](https://www.nuget.org/packages/CanFx.Mapping) | 0.1.0 | Oğuzhan Can | AutoMapper benzeri, lisans derdi olmayan nesne eşleyici: Profile/CreateMap/ForM… |
| 2026-10-21 14:55:37 | [CanFx.Templates](https://www.nuget.org/packages/CanFx.Templates) | 0.1.0 | Oğuzhan Can | CanFx paketlerini kullanan katmanlı monolith çözüm şablonu (dotnet new canfx-mo… |
| 2026-10-21 14:55:38 | [CanFx.Caching.Redis](https://www.nuget.org/packages/CanFx.Caching.Redis) | 0.1.0 | Oğuzhan Can | Redis'i HybridCache'in ikinci (dağıtık) katmanı yapar: birden fazla sunucu aynı… |
| 2026-10-21 14:55:38 | [CanFx.Mailing.MailKit](https://www.nuget.org/packages/CanFx.Mailing.MailKit) | 0.1.0 | Oğuzhan Can | IEmailSender'ın MailKit (MIT) ile SMTP implementasyonu ve geliştirme ortamı içi… |
| 2026-10-21 14:55:39 | [CanFx.EventBus.AzureServiceBus](https://www.nuget.org/packages/CanFx.EventBus.AzureServiceBus) | 0.1.0 | Oğuzhan Can | CanFx.EventBus için Azure Service Bus taşıyıcısı: topic + servis başına subscri… |
| 2026-10-21 14:55:40 | [CanFx.Realtime](https://www.nuget.org/packages/CanFx.Realtime) | 0.1.0 | Oğuzhan Can | Anlık bildirim soyutlaması (IRealtimeNotifier): kullanıcıya, role, tüm tenant'a… |
| 2026-10-21 14:55:41 | [CanFx.Testing.AspNetCore](https://www.nuget.org/packages/CanFx.Testing.AspNetCore) | 0.1.0 | Oğuzhan Can | API testleri için: istekte verilen kullanıcıyla (rol, yetki, tenant) kimlik doğ… |
| 2026-10-21 14:55:42 | [CanFx.Settings](https://www.nuget.org/packages/CanFx.Settings) | 0.1.0 | Oğuzhan Can | Tipli uygulama ve tenant ayarları: kodda tanım, tenant → uygulama → varsayılan… |
| 2026-10-21 14:55:45 | [CanFx.Testing.EntityFrameworkCore](https://www.nuget.org/packages/CanFx.Testing.EntityFrameworkCore) | 0.1.0 | Oğuzhan Can | Testler için bellekte çalışan gerçek ilişkisel veritabanı (SQLite): test başına… |
| 2026-10-21 14:55:45 | [CanFx.Mediator](https://www.nuget.org/packages/CanFx.Mediator) | 0.1.0 | Oğuzhan Can | MediatR'a benzer, lisans derdi olmayan hafif mediator: Send, Publish, Stream, p… |
| 2026-10-21 14:55:46 | [CanFx.WebApi](https://www.nuget.org/packages/CanFx.WebApi) | 0.1.0 | Oğuzhan Can | ASP.NET Core entegrasyonu: CanFx hata tiplerini ProblemDetails yanıtlarına çevi… |
| 2026-10-21 14:55:47 | [CanFx.EventBus](https://www.nuget.org/packages/CanFx.EventBus) | 0.1.0 | Oğuzhan Can | Integration event'leri servisler/örnekler arasında taşıyan event bus soyutlamas… |
| 2026-10-21 14:55:47 | [CanFx.Security.EntityFrameworkCore](https://www.nuget.org/packages/CanFx.Security.EntityFrameworkCore) | 0.1.0 | Oğuzhan Can | CanFx.Security entity'leri (User, Role, UserRole, RefreshToken, OTP/e-posta doğ… |
| 2026-10-21 14:55:48 | [CanFx.Application.Abstractions](https://www.nuget.org/packages/CanFx.Application.Abstractions) | 0.1.0 | Oğuzhan Can | Uygulama katmanının altyapıdan beklediği ortak sözleşmeler: ICurrentUser, ICurr… |
| 2026-10-21 14:55:49 | [CanFx.MultiTenancy](https://www.nuget.org/packages/CanFx.MultiTenancy) | 0.1.0 | Oğuzhan Can | Çoklu kiracılık: tenant bilgisi ve deposu, istek başına aktif tenant, tek verit… |
| 2026-10-21 14:55:49 | [CanFx.Search](https://www.nuget.org/packages/CanFx.Search) | 0.1.0 | Oğuzhan Can | Tam metin arama soyutlaması (ISearchIndex): sorgu, filtre, sıralama, vurgulama,… |
| 2026-10-21 14:55:50 | [CanFx.Settings.EntityFrameworkCore](https://www.nuget.org/packages/CanFx.Settings.EntityFrameworkCore) | 0.1.0 | Oğuzhan Can | Ayar değerleri için EF Core deposu ve tablo yapılandırması (SettingValues). |
| 2026-10-21 14:55:51 | [CanFx.EventBus.RabbitMQ](https://www.nuget.org/packages/CanFx.EventBus.RabbitMQ) | 0.1.0 | Oğuzhan Can | CanFx.EventBus için RabbitMQ taşıyıcısı: topic exchange, quorum kuyruk, gönderi… |
| 2026-10-21 14:55:51 | [CanFx.Reporting.AspNetCore](https://www.nuget.org/packages/CanFx.Reporting.AspNetCore) | 0.1.0 | Oğuzhan Can | Raporlama HTTP uçları: veri kaynakları ve alanları, rapor çalıştırma, CSV/Excel… |
| 2026-10-21 14:55:52 | [CanFx.Resilience.Http](https://www.nuget.org/packages/CanFx.Resilience.Http) | 0.1.0 | Oğuzhan Can | HttpClient için dayanıklılık: IHttpClientBuilder'a standart (toplam süre + retr… |
| 2026-10-21 14:55:52 | [CanFx.Sms](https://www.nuget.org/packages/CanFx.Sms) | 0.1.0 | Oğuzhan Can | SMS altyapısı: ISmsSender, telefon numarası normalleştirme (E.164), GSM-7/UCS-2… |
| 2026-10-21 14:55:53 | [CanFx.Mailing](https://www.nuget.org/packages/CanFx.Mailing) | 0.1.0 | Oğuzhan Can | E-posta gönderme sözleşmesi (IEmailSender, EmailMessage) ve testler/geliştirme… |
| 2026-10-21 14:55:54 | [CanFx.Resilience](https://www.nuget.org/packages/CanFx.Resilience) | 0.1.0 | Oğuzhan Can | Dış paket gerektirmeyen dayanıklılık (resilience) kütüphanesi: retry, circuit b… |
| 2026-10-21 14:55:54 | [CanFx.WebApi.OpenApi](https://www.nuget.org/packages/CanFx.WebApi.OpenApi) | 0.1.0 | Oğuzhan Can | OpenAPI belgeleri (Microsoft.AspNetCore.OpenApi): API sürümü başına belge, cook… |
| 2026-10-21 14:55:55 | [CanFx.Application](https://www.nuget.org/packages/CanFx.Application) | 0.1.0 | Oğuzhan Can | Uygulama katmanı altyapısı: CanFx.Mediator üzerinde logging, performans, yetkil… |
| 2026-10-21 14:55:55 | [CanFx.Security](https://www.nuget.org/packages/CanFx.Security) | 0.1.0 | Oğuzhan Can | Kimlik doğrulama yapı taşları: PBKDF2 şifre hash'leme, JWT access token, rotasy… |
| 2026-10-21 14:55:56 | [CanFx.FileStorage.S3](https://www.nuget.org/packages/CanFx.FileStorage.S3) | 0.1.0 | Oğuzhan Can | S3 uyumlu depolama (AWS S3, MinIO, Cloudflare R2, Wasabi ...) için IFileStorage… |
| 2026-10-21 14:55:57 | [CanFx.Generator.Cli](https://www.nuget.org/packages/CanFx.Generator.Cli) | 0.1.0 | Oğuzhan Can | can-gen: CanFx çözümlerinde entity'den CRUD (CQRS) kodu üreten komut satırı ara… |
| 2026-10-21 14:55:58 | [CanFx.Logging.Serilog](https://www.nuget.org/packages/CanFx.Logging.Serilog) | 0.1.0 | Oğuzhan Can | Serilog ile yapılandırılmış loglama: makul varsayılanlar (geliştirmede okunur k… |
| 2026-10-21 14:57:55 | [Polyadic.CodeStyle](https://www.nuget.org/packages/Polyadic.CodeStyle) | 1.2.0 | Polyadic | Various analyzers bundled with opinionated configuration |
| 2026-10-21 14:59:21 | [LMI.Media](https://www.nuget.org/packages/LMI.Media) | 1.0.0 | Lyubimov Mikhail Igorevich | Минималистичная библиотека для работы с медиа |
| 2026-10-21 15:04:17 | [Mdf4Net](https://www.nuget.org/packages/Mdf4Net) | 0.1.0 | Dietmar Borgards | Read and write ASAM MDF 4.x (MF4) measurement data files in pure .NET: sorted a… |
| 2026-10-21 15:05:20 | [IO3.Identity.Service.SDK](https://www.nuget.org/packages/IO3.Identity.Service.SDK) | 3.0.0 | IO3.Identity.Service.SDK | Package Description |
| 2026-10-21 15:10:31 | [Pqax.Collector](https://www.nuget.org/packages/Pqax.Collector) | 0.1.0 | SQLBI | Collects the footprint of Delta tables from OneLake or from a local folder: rea… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
