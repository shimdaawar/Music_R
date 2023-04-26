from date_time import *

def taggen(tags,detected_mood):
    tag=[]
    tag=tags
    tag.append(detected_mood)
    tag2=set(tag)
    tag=[]
    for i in tag2:
        tag.append(i)
    tag1=[]
    for i in tag:
        tag1.append(i)


    time=time_slot

    weth=w_final
    final_tag=[]
    if len(tag1)==4:
        final_tag.append(tag1[3])
        if weth=="CS":
                if time=="M":
                    final_tag+=["Angry","Neutral","Happy"]
                elif time=="A":
                    final_tag+=["Happy","Angry","Neutral"]
                elif time=="E":
                    final_tag+=["Neutral","Angry","Happy"]
                else:
                    final_tag+=["Neutral","Angry","Happy"]
        elif weth=="C":
            if time=="M":
                final_tag+=["Sad","Happy","Neutral"]
            elif time=="A":
                final_tag+=["Happy","Sad","Neutral"]
            elif time=="E":
                final_tag+=["Sad","Neutral","Happy"]
            else:
                final_tag+=["Neutral","Sad","Happy"]
        elif weth=="R" or weth=="M":
            if time=="M":
                final_tag+=["Sad","Neutral","Fear"]
            elif time=="A":
                final_tag+=["Neutral","Sad","Fear"]
            elif time=="E":
                final_tag+=["Neutral","Sad","Fear"]
            else:
                final_tag+=["Fear","Sad","Neutral"]
        else:
            if time=="M":
                final_tag+=["Neutral","Fear","Happy"]
            elif time=="A":
                final_tag+=["Happy","Fear","Neutral"]
            elif time=="E":
                final_tag+=["Happy","Fear","Neutral"]
            else:
                final_tag+=["Fear","Neutral","Happy"]
            

    if len(tag1)==3:
        if weth=="CS":
            if time=="M":
                final_tag=["Angry","Neutral","Happy"]
            elif time=="A":
                final_tag=["Happy","Angry","Neutral"]
            elif time=="E":
                final_tag=["Neutral","Angry","Happy"]
            else:
                final_tag=["Neutral","Angry","Happy"]
        elif weth=="C":
            if time=="M":
                final_tag=["Sad","Happy","Neutral"]
            elif time=="A":
                final_tag=["Happy","Sad","Neutral"]
            elif time=="E":
                final_tag=["Sad","Neutral","Happy"]
            else:
                final_tag=["Neutral","Sad","Happy"]
        elif weth=="R" or weth=="M":
            if time=="M":
                final_tag=["Sad","Neutral","Fear"]
            elif time=="A":
                final_tag=["Neutral","Sad","Fear"]
            elif time=="E":
                final_tag=["Neutral","Sad","Fear"]
            else:
                final_tag=["Fear","Sad","Neutral"]
        else:
            if time=="M":
                final_tag=["Neutral","Fear","Happy"]
            elif time=="A":
                final_tag=["Happy","Fear","Neutral"]
            elif time=="E":
                final_tag=["Happy","Fear","Neutral"]
            else:
                final_tag=["Fear","Neutral","Happy"]
    return final_tag