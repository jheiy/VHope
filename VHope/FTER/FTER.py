from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

PATH = '/home/jacky/Documents/GitHub/VHope/VHope/FTER/fter-medium-2'

tokenizer = AutoTokenizer.from_pretrained(PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(PATH, local_files_only=True)

# tokenizer = AutoTokenizer.from_pretrained("fter-medium-2")
# model = AutoModelForCausalLM.from_pretrained("fter-medium-2")

class FTER:
  def generate(self, retrieved):
    # chat
    for step in range (1):
      # encode the new user input, add the eos_token and return a tensor in Pytorch
      new_user_input_ids = tokenizer.encode(retrieved + tokenizer.eos_token, return_tensors='pt')

      # append the new user input tokens to the chat history
      bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

      # generated a response while limiting the total chat history to 1000 tokens    
      chat_history_ids = model.generate(
          bot_input_ids, max_length=1000,
          pad_token_id=tokenizer.eos_token_id,  
          no_repeat_ngram_size=3,       
          do_sample=True, 
          top_k=100, 
          top_p=0.7,
          temperature = 0.8
      )

      # pretty print last ouput tokens from bot
      # print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
      return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


# if __name__ == "__main__":
#   fter = FTER()
#   sample_text = "I feel so sad today eof Is there anything else you can say about that? eof I feel so sad today "
#   print(fter.generate(sample_text))