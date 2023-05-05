import streamlit as st

st.title("PERHITUNGAN KONSENTRASI MOLAR dan MOLAL SUATU LARUTAN")
st.write("PERHITUNGAN mol ZAT TERLARUT")

gram = st.number_input('Masukkan massa senyawa (g)')
Mr = st.number_input('Masukkan Mr senyawa')

tombol = st.button('Hitung nilai mol zat terlarut')

if tombol:
    nilai_mol_zat_terlarut = gram/mr
    st.success(f'nilai mol zat terlarut adalah {nilai_mol_zat_terlarut}')

st.write("PERHITUNGAN KONSENTRASI MOLAR LARUTAN")

MOL = st.number_input('Masukkan mol zat terlarut')
VOLlarutan = st.number_input('Masukkan volume larutan (L)')

tombol = st.button('Hitung nilai konsentrasi molar')

if tombol:
    nilai_konsentrasi_molaritas = MOL/VOLlarutan
    st.success(f'nilai konsentrasi molar adalah {nilai_konsentrasi_molaritas}')
    
st.write("PERHITUNGAN KONSENTRASI MOLAL LARUTAN")

MOL2 = st.number_input('Masukkan mol zat terlarut.')
kgPelarut = st.number_input('Masukkan kg pelarut')

tombol = st.button('Hitung nilai konsentrasi molal')

if tombol:
    nilai_konsentrasi_molal = MOL2/kgPelarut
    st.success(f'nilai konsentrasi molal adalah {nilai_konsentrasi_molal}')
   