import '../styles/InputBar.css';

function InputBar() {
  return (
    <div className="input-area">
      <div className="input-wrapper">
        <input
          type="text"
          placeholder="Type a message..."
          className="message-input"
        />
        <button className="send-btn">➤</button>
      </div>
    </div>
  );
}

export default InputBar;