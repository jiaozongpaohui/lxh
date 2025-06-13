import streamlit as st
from datetime import datetime, time
st.set_page_config(page_title='个人简历生成器',page_icon='🎨',layout='wide')
st.title("🎨个人简历生成器")
st.text('使用Streamlit创建您的个性化简历')
c1,c2=st.columns([1,2])
def my_format_func(option):
    return f'{option}'
with c1:
    st.subheader("个人信息表单")
    st.session_state['name'] = st.text_input('姓名',key='xm')
    st.session_state['post'] = st.text_input('职位')
    st.session_state['phone'] = st.text_input('电话')
    st.session_state['email'] = st.text_input('邮箱')
    st.session_state['birth'] = st.text_input('出生日期')
        
    xb = st.radio('性别:',['男', '女', '其他'],horizontal=True,format_func=my_format_func,key="gender")
    xl = st.selectbox('学历', ['大专', '本科', '硕士'], format_func=my_format_func, index=2,key="edu")
    yynl= st.multiselect('语言能力：', ['中文', '英文', '法语','俄语'],format_func=my_format_func,key="lang")
    jn= st.multiselect('技能：', ['Java', 'Python', 'c语言','机器学习'],format_func=my_format_func,key="jnzy")
    gzjy = st.slider('工作经验（年）', 0, 30,key="years")
    values = st.slider('期望薪资范围',3000, 30000, (6000, 15000),key="money")
    st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...',key="into")
    sj = st.time_input("每日最佳联系时间段", time(20, 45),key="Time")
    uploaded_avatar = st.file_uploader("上传头像（支持JPG/PNG）", type=["jpg", "png", "jpeg"])
with c2:
    st.subheader("简历实时预览")
    cc1, cc2= st.columns([1, 1])
    with cc1:
        st.markdown(f"姓名:{st.session_state['name']}")
        if uploaded_avatar:
            st.image(uploaded_avatar, width=150)
        st.markdown(f"🏢职位:{st.session_state['post']}")
        st.markdown(f"📞电话:{st.session_state['phone']}")
        st.markdown(f"📮邮箱:{st.session_state['email']}")
        st.markdown(f"📅出生日期:{st.session_state['birth']}")
    with cc2:
        st.markdown(f"⚥性别:{st.session_state.gender}")
        st.markdown(f"📚学历：{st.session_state.edu}")
        st.markdown(f"💬语言能力：{', '.join(st.session_state.lang)}")
        st.markdown(f"🏢工作经验：{st.session_state.years} 年")
        st.markdown(f"💰期望薪资：{st.session_state.money[0]} ~ {st.session_state.money[1]} 元")
        st.markdown(f"🕐最佳联系时间：{st.session_state.Time}")
    st.subheader("个人简介")
    st.markdown(f"\n{st.session_state.into}")
    st.subheader("专业技能")
    st.markdown(f"{', '.join(st.session_state.jnzy)}",unsafe_allow_html=True)
