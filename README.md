# Auto-GPT-Detective-Plugin
The Auto-GPT-Detective-Plugin is a useful tool for any AI enthusiast. 
This plugin aims to provide Auto-GPT with the ability to detect whether text is AI generated.
This will help the system recognize the quality of sources it is using.

### Key Features
- [Sapling AI Detector](https://sapling.ai/ai-content-detector): Detects whether text is ai generated with the ability to rate specific portions. Requires a Sapling AI paid plan in order to use the API.
- [ZeroGPT](https://www.zerogpt.com): Detects whether text is ai generated with the ability to rate specific portions. Requires API credentials in order to use the API (taken in as a json of POST headers).

### How It Works
If the environment variables for the detective engine (`DETECTIVE_ENGINE`) and the associated engine variables are set (documented below), the detective commands for that engine will be enabled.

### TODO
- [x] Implement initial detection through SaplingAI (It has a free trial for the API)
- [x] Implement [ZeroGPT](https://www.zerogpt.com) support
- [ ] Implement other detective engines ([GPTZero](https://gptzero.me)? [OpenAI](https://platform.openai.com/ai-text-classifier)? [Writer](https://writer.com/ai-content-detector/)?)
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

Put the following in your `.env` and uncomment as desired:

```env
################################################################################
### DETECTIVE PLUGIN SETTINGS
################################################################################

## DETECTIVE_ENGINE can be one of the following: saplingapi, zerogpt
# DETECTIVE_ENGINE=saplingai

## saplingapi mode requires a paid mode api key
## SAPLING_API_KEY is REQUIRED
## SAPLINGAI_POST_ENDPOINT is optional (defaults to https://api.sapling.ai/api/v1/aidetect)

# SAPLING_API_KEY=<insert_api_key_here>
# SAPLINGAI_POST_ENDPOINT=https://api.sapling.ai/api/v1/aidetect

## zerogpt requires the path to a json file that contains valid POST headers
## Due to the reserved nature of zerogpt's use, the correct format for an API key is unknown
## ZEROGPT_HEADER_JSON_PATH is REQUIRED
## ZEROGPT_POST_ENDPOINT is optional (defaults to https://api.zerogpt.com/api/detect/detectText)

# ZEROGPT_HEADER_JSON_PATH=<insert_path_here>
# ZEROGPT_POST_ENDPOINT=https://api.zerogpt.com/api/detect/detectText

```
