import openai
import streamlit as st
from openai import OpenAI
from openai import AssistantEventHandler



#assistant_id = "asst_XYgHWyKYN1KxNWfcN9EMdn2Q"        #replace with your own assistant
client = OpenAI(st.secrets["api_key"])   #Replace with your own API


st.title("💬 AeroGPT")
st.caption("🚀 Choose your Assistant!")

# Set the assistant ID and initialize the OpenAI client with your API key
assistant_options = {
    "Genel Asistan": "asst_XYgHWyKYN1KxNWfcN9EMdn2Q",   
    "Teknik Asistan": "asst_AdifferentAssistantID",  
    "DWH Asistan": "asst_YetAnotherAssistantId"  
}

selected_assistant = st.radio("Choose an Assistant:", list(assistant_options.keys()))
assistant_id = assistant_options[selected_assistant]


prompt = st.text_input("Enter your message")

if prompt:
    st.markdown("----")
    res_box = st.empty()
    report = []
    # thread = client.beta.threads.create()
    stream = client.beta.threads.create_and_run(
  assistant_id=assistant_id,
  thread={
    "messages": [
      {"role": "user", "content": prompt}
    ]
  },
  stream=True
)

    for event in stream:
        if event.data.object == "thread.message.delta":
            # Iterate over content in the delta
            for content in event.data.delta.content:
                if content.type == 'text':
                    # Print the value field from text deltas
                    report.append(content.text.value)
                    print(content.text.value)
                    result = "".join(report).strip()
                    # result = result.replace("\n", "")
                    res_box.markdown(f'*{result}*')

