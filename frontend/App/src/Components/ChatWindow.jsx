import '../styles/ChatWindow.css';
import MessageBubble from './MessageBubble';

const messages = [
  { id: 1, sender: 'bot',  text: 'Hey! 👋 Welcome to NexusAI Support. How can I help you today?' },
  { id: 2, sender: 'user', text: 'I need help with my order. It hasn\'t arrived yet.' },
  { id: 3, sender: 'bot',  text: 'Sorry to hear that! Could you share your order ID so I can look into it?' },
  { id: 4, sender: 'user', text: 'Sure, it\'s #4521.' },
  { id: 5, sender: 'bot',  text: 'Got it, looking that up for you right now...' },
];

function ChatWindow() {
  return (
    <>
      <div className="chat-header-bar">
        <div className="header-bot-info">
          <div className="header-avatar">
            AI
            <div className="header-online-dot"></div>
          </div>
          <div>
            <div className="header-name">Support Agent</div>
            <div className="header-active">● Active now</div>
          </div>
        </div>
      </div>

      <div className="chat-window">
        <div className="date-divider">
          <hr /><span>Today</span><hr />
        </div>
        {messages.map(({ id, sender, text }) => (
          <MessageBubble key={id} sender={sender} text={text} />
        ))}
      </div>
    </>
  );
}

export default ChatWindow;