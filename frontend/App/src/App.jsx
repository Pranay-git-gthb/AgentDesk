import './App.css';
import Sidebar from './components/Sidebar';
import ChatWindow from './components/ChatWindow';
import InputBar from './components/InputBar';

function App() {
  return (
    <div className="app">
      <Sidebar />
      <div className="main">
        <ChatWindow />
        <InputBar />
      </div>
    </div>
  );
}

export default App;