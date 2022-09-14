import streamlit as st
from src.medallia import run_app, per_score



st.title('Team Metrics')


choice = st.selectbox('Team', ['Koscom', 'Beon Connect', 'Internal', 'UKR'], help='Select Team')
k_fail, k_pass, k_pww, s_fail, s_pass, s_pww, u_fail, u_pass, u_pww, b_fail, b_pass, b_pww, kos_nps, sbi_nps, beon_nps, ukr_nps, k_pht, s_pht, b_pht, u_pht, d = run_app()

st.header('Team NPS')

if choice == 'Koscom':
    st.subheader(f'{choice} NPS score is {per_score(kos_nps)}')
elif choice == 'Beon Connect':
    st.subheader(f'{choice} NPS score is {per_score(beon_nps)}')
elif choice == 'Internal':
    st.subheader(f'{choice} NPS score is {per_score(sbi_nps)}')
elif choice == 'UKR':
    st.subheader(f'{choice} NPS score is {per_score(ukr_nps)}')

st.header('Team PHT')
if choice == 'Koscom':
    st.subheader(f'{choice} Pure pass percentage is {round(k_pass/(k_pht.sum())* 100, 2)}%.')
    st.write(f'{choice} has {k_pass} pure pass jobs.')
    st.write(f'{choice} has {k_pww} pass with warnings jobs.')
    st.write(f'{choice} has {k_fail} failed jobs.')
elif choice == 'Beon Connect':
    st.subheader(f'{choice} Pure pass percentage is {round(b_pass/(b_pht.sum())* 100, 2)}%.')
    st.write(f'{choice} has {b_pass} pure pass jobs.')
    st.write(f'{choice} has {b_pww} pass with warnings jobs.')
    st.write(f'{choice} has {b_fail} failed jobs.')
elif choice == 'Internal':
    st.subheader(f'{choice} Pure pass percentage is {round(s_pass/(s_pht.sum())* 100, 2)}%.')
    st.write(f'{choice} has {s_pass} pure pass jobs.')
    st.write(f'{choice} has {s_pww} pass with warnings jobs.')
    st.write(f'{choice} has {s_fail} failed jobs.')
elif choice == 'UKR':
    st.subheader(f'{choice} Pure pass percentage is {round(u_pass/(u_pht.sum())* 100, 2)}%.')
    st.write(f'{choice} has {u_pass} pure pass jobs.')
    st.write(f'{choice} has {u_pww} pass with warnings jobs.')
    st.write(f'{choice} has {u_fail} failed jobs.')



# st.header('Team FTR')
