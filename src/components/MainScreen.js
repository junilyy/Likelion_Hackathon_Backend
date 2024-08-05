import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import logoIcon from './logo.png';
import { FaDumbbell, FaUtensils, FaUser } from 'react-icons/fa';

const containerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  height: '100vh',
  paddingTop: '5%',
  fontFamily: 'Noto Sans KR, sans-serif',
  backgroundColor: '#f0f4f8',
};

const logoStyle = {
  marginBottom: '40px',
  width: '80px',
  borderRadius: '50%',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
};

const buttonStyle = {
  marginBottom: '20px',
  padding: '10px 20px',
  backgroundColor: 'transparent',
  border: '2px solid #007bff',
  borderRadius: '30px',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  fontSize: '16px',
  fontWeight: 'bold',
  width: '200px',
  cursor: 'pointer',
  transition: 'background-color 0.3s, color 0.3s, transform 0.3s',
  position: 'relative',
  overflow: 'hidden',
  textDecoration: 'none',
  color: '#007bff',
};

const iconStyle = {
  marginRight: '10px',
  fontSize: '20px',
};

const textStyle = {
  display: 'inline-block',
  flex: 1,
  textAlign: 'center',
};

const hoverCircleStyle = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  width: '200%',
  height: '200%',
  backgroundColor: 'rgba(0, 123, 255, 0.1)',
  borderRadius: '50%',
  transform: 'translate(-50%, -50%) scale(0)',
  transition: 'transform 0.3s',
  pointerEvents: 'none',
  zIndex: 1,
};

const footerStyle = {
  marginTop: '10px', // Adjust this margin to place the footer closer to the "내 정보" button
  padding: '20px',
  textAlign: 'center',
};

const linkStyle = {
  margin: '0 10px',
  cursor: 'pointer',
  color: '#007bff',
  textDecoration: 'none',
  fontSize: '16px',
  transition: 'color 0.3s',
};

const applyHoverEffect = (buttonRef, hoverCircleRef) => {
  buttonRef.addEventListener('mouseenter', () => {
    hoverCircleRef.style.transform = 'translate(-50%, -50%) scale(1)';
    buttonRef.style.backgroundColor = '#007bff';
    buttonRef.style.color = '#ffffff';
  });

  buttonRef.addEventListener('mouseleave', () => {
    hoverCircleRef.style.transform = 'translate(-50%, -50%) scale(0)';
    buttonRef.style.backgroundColor = 'transparent';
    buttonRef.style.color = '#007bff';
  });
};

const ButtonWithHoverEffect = ({ onClick, icon: Icon, text }) => {
  const buttonRef = useRef(null);
  const hoverCircleRef = useRef(null);

  useEffect(() => {
    applyHoverEffect(buttonRef.current, hoverCircleRef.current);
  }, []);

  return (
    <button ref={buttonRef} style={buttonStyle} onClick={onClick}>
      <div ref={hoverCircleRef} style={hoverCircleStyle}></div>
      <Icon style={iconStyle} /> <span style={textStyle}>{text}</span>
    </button>
  );
};

const MainScreen = ({ onExerciseRecommendation }) => {
  const navigate = useNavigate();

  return (
    <div style={containerStyle}>
      <img src={logoIcon} alt="Logo Icon" style={logoStyle} />
      <ButtonWithHoverEffect onClick={onExerciseRecommendation} icon={FaDumbbell} text="운동 추천" />
      <ButtonWithHoverEffect icon={FaUtensils} text="음식 추천" onClick={() => navigate('/map')} />
      <ButtonWithHoverEffect icon={FaUser} text="내 정보" onClick={() => navigate('/state1')} />
      <div style={footerStyle}>
        <span style={linkStyle} onClick={() => navigate('/page1')}>로그인</span>
        <span style={linkStyle} onClick={() => navigate('/page2')}>회원가입</span>
      </div>
    </div>
  );
};

export default MainScreen;
