# Auto-GPT-Detective-Plugin
The Auto-GPT-Detective-Plugin is a useful tool for any AI enthusiast. 
This plugin aims to provide Auto-GPT with the ability to detect whether text is AI generated.
This will help the system recognize the quality of sources it is using.

### Key Features
- [Sapling AI Detector](https://sapling.ai/ai-content-detector): Detects whether text is ai generated, with the ability to rate specific portions. Requires a Sapling AI paid plan in order to use the API.

### How It Works
If the environment variables for the detective engine (`DETECTIVE_ENGINE`) and the associated api key (`SAPLINGAI_API_KEY`) are set, the detective commands for that engine will be enabled.

### TODO
- [x] Implement initial detection through SaplingAI (It has a free trial for the API)
- [ ] Implement other detective engines ([GPTZero](https://gptzero.me)? [ZeroGPT](https://www.zerogpt.com)? [OpenAI](https://platform.openai.com/ai-text-classifier)? [Writer](https://writer.com/ai-content-detector/)?)
- [ ] Format the engine output to be consistent across the engines


### Plugin Installation Steps
Download this repository as a .zip file, copy it to ./plugins/, and rename it to Auto-GPT-Detective-Plugin.zip.

To download it directly from your Auto-GPT directory, you can run this command on Linux or MacOS:
```sh
curl -o ./plugins/Auto-GPT-Detective-Plugin.zip https://github.com/amrrsn/Auto-GPT-Detective-Plugin/archive/refs/heads/master.zip
```

In PowerShell:
```pwsh
Invoke-WebRequest -Uri "ttps://github.com/amrrsn/Auto-GPT-Detective-Plugin/archive/refs/heads/master.zip" -OutFile "./plugins/Auto-GPT-Detective-Plugin.zip"
```

Put the following in your `.env`

```env
################################################################################
### DETECTIVE PLUGIN SETTINGS
################################################################################

DETECTIVE_ENGINE=saplingapi
SAPLING_API_KEY=<insert_api_key_here>
```
