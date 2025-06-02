from flask import Flask, request, jsonify
from llm_prompt import parse_vm_request
from proxmox_handler import create_vm
import json

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/create-vm', methods=['POST'])
def create_vm_from_prompt():
    user_input = request.json.get('prompt')
    llm_output = parse_vm_request(user_input)

    try:
        import re
        match = re.search(r"\{[\s\S]*\}", llm_output)
        if match:
            json_str = match.group(0)
        else:
            raise ValueError("No valid JSON object found in LLM output")

        vm_config = json.loads(json_str)
        create_vm(vm_config)
        return jsonify({"status": "VM creation triggered", "config": vm_config})
    except Exception as e:
        return jsonify({"error": str(e), "llm_output": llm_output}), 400

if __name__ == "__main__":
    app.run(debug=True)