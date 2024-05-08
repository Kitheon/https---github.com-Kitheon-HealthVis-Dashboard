import streamlit as st

# Define the steps of recovery and their corresponding descriptions
recovery_steps = [
    {"step": "Admittance", "description": "This is an admission that you need help with your addiction."},
    {"step": "Belief", "description": "Understanding and believing that you are worthy of sobriety, and are capable of achieving it."},
    {"step": "Desire to Change", "description": "Willingness to try various things in order to find what will help you."},
    {"step": "Self-Inventory", "description": "Examine yourself to determine what has caused you to become an addict."},
    {"step": "Reflection", "description": "Reflect on the negatives in your life, and possibly discuss them with someone else."},
    {"step": "Surrender", "description": "Being willing to give up self-destructive thoughts and actions, and end relationships with people that are harmful to your sobriety."},
    {"step": "Action", "description": "Enact the changes necessary to help you get your life back on track."},
    {"step": "List", "description": "List all of the people your addiction has harmed."},
    {"step": "Amends", "description": "Make direct amends to the people on your list, unless doing so would cause further harm."},
    {"step": "Continued Reflection", "description": "Regularly re-examine yourself and your life to assure that negative habits are not recurring."},
    {"step": "Involvement", "description": "Find new, positive habits and people to replace the negative ones."},
    {"step": "Moral Compass", "description": "Give back, and otherwise live a clean, kind, and upstanding existence."}
]

smdict = {
    1: "Do you accept that you need help with your addiction?",
    2: "Do you believe that you are capable of sobriety, and will be able to achieve it one day?",
    3: "Are you willing to try different methods until you are able to become sober?",
    4: "Do you understand why you have become an addict?",
    5: "Have you discussed the negative aspects of your life with those around you, and do you wish to change them?",
    6: "Are you willing to stop any self-destructive thoughts and actions, and cut yourself off from bad influences for the sake of your sobriety?",
    7: "Have you taken the steps you know to be necessary in order to get your life back on track?",
    8: "Have you made a list of all the people who your addiction has harmed?",
    9: "Have you made amends with every person on this list?",
    10: "Have you had enough time to make sure that you have rid yourself of your destructive habits?",
    11: "Have you developed any positive habits which can replace the negative ones you have given up?",
    12: "Are you living an upstanding life, giving back to those who have helped you when you can, and staying clear of harmful substances?"
}

msgDict = {
    1: "The first step to recovering from addiction is accepting that you suffer from it.  Admit to others and to yourself that you have an addiction.",
    2: "In order to change, you must believe that change is possible. Move onto the next step once you have learned that you are able to change.",
    3: "The next step is the desire for change. Think of all of the positive effects which sobriety will bring to yourself and those around you.",
    4: "To understand your addiction, understand what brought you down this path in the first place. By knowing this, you can prevent yourself from making the same mistakes again.",
    5: "Reflect on the harm which your addiction has brought. This will help bolster your desire for change.",
    6: "Cut yourself from everything which can cause a relapse, including any people you know to be detrimental to your sobriety.",
    7: "Part of the reason which you have chosen the path of sobriety is to get your life back to where you want it to be. Now that you have distanced yourself from your addiction, take the time to get your life back.",
    8: "Your addiction has been harmful to those around you. Recognize the people who your destructive habits have hurt.",
    9: "Simply knowing who you have hurt is not enough. Now you must make up for the harm your habits have caused these people.",
    10: "The path to complete sobriety takes time. Make sure to take the time to be certain that you have gotten rid of your destructive habits.",
    11: "Negative habits may reoccur if nothing takes their place. Find positive habits which can fill this gap, and find new positive influences to replace the negative ones which you have cut off.",
    12: "You have not undergone this journey alone. Others have helped you get here, so be sure to give back to these people, and to help those who wish to take the same path you have.",
    13: "Congratulations! You have completed all 12 steps. Be proud of how far you have come, and avoid falling into the same habits once again."
}

def main():
    # Display the timeline
    st.write("### Twelve Steps to Recovery Timeline")

    if "nsteps" not in st.session_state:
        st.session_state.nsteps = 1
    st.session_state.yesBtn = False

    for idx, step in enumerate(recovery_steps[: st.session_state.nsteps]):
        # Determine circle size based on whether it's the current step or not
        circle_size = 40 if idx == st.session_state.nsteps-1 else 30
        
        # Apply larger font size for the current step
        font_size = "1.2em" if idx == st.session_state.nsteps-1 else "1em"
        
        # Apply different colors for the current step and others
        circle_color = "#3182bd" if idx == st.session_state.nsteps-1 else "#9ecae1"
        text_color = "white" if idx == st.session_state.nsteps-1 else "black"
        
        st.markdown(
            f"""<div style="display: flex; align-items: center;">
                <div style="background-color: {circle_color}; color: {text_color}; border-radius: 50%; width: {circle_size}px; height: {circle_size}px; 
                display: flex; align-items: center; justify-content: center; margin-right: 10px; font-size: {font_size};">
                {idx + 1}
                </div>
                <div>
                <h3>{step['step']}</h3>
                <p>{step['description']}</p>
                </div>
            </div>""",
            unsafe_allow_html=True
        )
    if st.session_state.nsteps < 13:
        st.write(smdict[st.session_state.nsteps])
        col1, col2 = st.columns(2)
        st.session_state.yesBtn = col1.button("Yes", key=st.session_state.nsteps)
        if col2.button("No"):
            st.progress((st.session_state.nsteps-1)/12)
            st.write(f"You are {13-st.session_state.nsteps} steps away from reaching your goal of sobriety.")
            st.write(msgDict[st.session_state.nsteps])
        elif st.session_state.yesBtn:
            st.session_state.yesBtn = False
            st.session_state.nsteps += 1
            if st.session_state.nsteps == 13:
                st.progress((st.session_state.nsteps-1)/12)
                st.write(msgDict[13])
            st.rerun()
    else:
        st.progress((st.session_state.nsteps-1)/12)
        st.write(msgDict[13])
    

# https://www.12step.com/articles/12-step-programs-for-atheists
# I wanted to choose a non-religious plan. a lot of the plans were religious, but the non-religious ones should work for everybody.