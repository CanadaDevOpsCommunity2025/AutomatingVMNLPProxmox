import requests
import re

def parse_vm_request(prompt):
    HF_TOKEN = "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"  # Replace this with your real token
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": f"Convert this natural language VM request to JSON:\n{prompt}",
        "parameters": {"max_new_tokens": 200}
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    print("HF Response Status:", response.status_code)
    print("HF Response Text:", response.text)

    try:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            llm_output = result[0]["generated_text"]
        else:
            raise RuntimeError(f"Unexpected response format: {result}")

        match = re.search(r"\{[\s\S]*\}", llm_output)
        if match:
            json_str = match.group(0).strip()
            try:
                import json
                json.loads(json_str)  # Validate it's complete JSON
            except json.JSONDecodeError as e:
                raise ValueError(f"Malformed JSON extracted: {e}")
            return json_str
        else:
            raise ValueError("No valid JSON object found in LLM output")
    except Exception as e:
        raise RuntimeError(f"HF API failed: {e}")