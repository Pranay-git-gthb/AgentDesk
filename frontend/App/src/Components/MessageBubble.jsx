import '../styles/MessageBubble.css';

function MessageBubble({ sender, text }) {
  return (
    <div className={`msg-row ${sender}`}>
      {sender === 'bot' && <div className="msg-avatar">AI</div>}
      <div className="msg-content">
        <div className={`bubble ${sender}`}>{text}</div>
        <div className="msg-time">just now</div>
      </div>
    </div>
  );
}

export default MessageBubble;