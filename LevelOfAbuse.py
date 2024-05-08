import streamlit as st

ABUSELEVEL = 0
global_state = {"state": 1}

# Lists for checkboxes on each page
l1 = ['You have are curious about drugs.',
      'Your peers pressure you to take drugs.']

l2 = ['You use drugs at parties.',
      'You use drugs when stressed.']

l3 = ['You use drugs on regular occasions.',
      'You see school/work as dispensible, and escaping into a drugged condition becomes a regular occurence.']

l4 = ['Drug usage has regular and negative consequences.',
      'You have driven a vehicle while under the influence of drugs',
      'Performance at school or work has deteriorated due to drug usage.',
      'You have dropped old friends in favor of friends with similar drug habits.'
      ]

l5 = ['You need to consume more and more drugs to feel "okay"',
      'Going without drugs causes the pain of withdrawal']

l6 = ["You cannot face life without using drugs.",
      "Drug use can't be controlled.",
      "Negative consequences of drug usage do not stop the usage of drugs.",
      ]

ALDict = {
    0: "Stage 0: No Interest",
    1: "Stage 1: Introduction to Drugs",
    2: "Stage 2: Experimentation",
    3: "Stage 3: Regular Usage",
    4: "Stage 4: Problem Use",
    5: "Stage 5: Drug Dependence",
    6: "Stage 6: Active Dependency"
}
ALDict2 = {
    0: "You have no interest in doing drugs, and no one pressures you to take them.",
    1: "You want to try drugs or have friends which want you to try drugs. Consider the negative effects which drugs will bring.",
    2: "You use drugs in certain circumstances. Be careful not to make it a habit.",
    3: "You use drugs on regular occasion.  Cut back while you still can.",
    4: "Your drug habits are beginning to have a negative impact on your life.  Stop abusing drugs before you cause too much damage.",
    5: "You have a physical and psychological dependence on drugs.  Seek counceling.",
    6: "Drugs have become a necessity for day-to-day life.  Seek professional help immediately."
}

def main():
    st.title("Abuse Level Survey")

    st.write("Check the boxes that apply to you. Then press Next.")
    st.write("Continue until you get your drug abuse level.")
    st.write(" ")

    # Initialize session state if it doesn't exist
    if "state" not in st.session_state:
        st.session_state.state = 1
    if "AL" not in st.session_state:
        st.session_state.AL = 6
    st.session_state.rerun = False
    st.session_state.btn = False

    STATE = st.session_state.state

    if STATE == 1:
        selected_options1 = [option for option in l6 if st.checkbox(option)]
        num_checked1 = len(selected_options1)
        n1 = st.button("Next", key="n1")
        if n1:
            n1 = False
            st.session_state.rerun = True
            if num_checked1 == 0:
                STATE = 2
                st.session_state.AL = 5
            else:
                STATE = 7
    elif STATE == 2:
        selected_options2 = [option for option in l5 if st.checkbox(option)]
        num_checked2 = len(selected_options2)
        n2 = st.button("Next", key="n2")
        if n2:
            n2 = False
            st.session_state.rerun = True
            if num_checked2 == 0:
                STATE = 3
                st.session_state.AL = 4
            else:
                STATE = 7
    elif STATE == 3:
        selected_options3 = [option for option in l4 if st.checkbox(option)]
        num_checked3 = len(selected_options3)
        n3 = st.button("Next", key="n3")
        if n3:
            st.session_state.rerun = True
            if num_checked3 == 0:
                STATE = 4
                st.session_state.AL = 3
            else:
                STATE = 7
    elif STATE == 4:
        selected_options4 = [option for option in l3 if st.checkbox(option)]
        num_checked4 = len(selected_options4)
        n4 = st.button("Next", key="n4")
        if n4:
            st.session_state.rerun = True
            if num_checked4 == 0:
                STATE = 5
                st.session_state.AL = 2
            else:
                STATE = 7
    elif STATE == 5:
        selected_options5 = [option for option in l2 if st.checkbox(option)]
        num_checked5 = len(selected_options5)
        n5 = st.button("Next", key="n5")
        if n5:
            st.session_state.rerun = True
            if num_checked5 == 0:
                STATE = 6
                st.session_state.AL = 1
            else:
                STATE = 7
    elif STATE == 6:
        selected_options6 = [option for option in l1 if st.checkbox(option)]
        num_checked6 = len(selected_options6)
        n6 = st.button("Next", key="n6")
        if n6:
            st.session_state.rerun = True
            if num_checked6 == 0:
                STATE = 7
                st.session_state.AL = 0
            else:
                STATE = 7
    elif STATE == 7:
        if st.session_state.AL < 3:
            st.progress(st.session_state.AL / 6)
        elif st.session_state.AL < 5:
            st.progress(st.session_state.AL / 6)
        else:
            st.progress(st.session_state.AL / 6)
        st.write(ALDict[st.session_state.AL])
        st.write(ALDict2[st.session_state.AL])

    st.session_state.state = STATE
    if st.session_state.rerun:
        st.session_state.rerun = False
        st.rerun()

if __name__ == "__main__":
    main()


# source: https://www.buckeyeclinic.com/six-stages-drug-addiction/