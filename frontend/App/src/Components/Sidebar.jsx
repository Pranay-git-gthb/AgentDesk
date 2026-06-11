import '../styles/Sidebar.css';

function Sidebar() {
  return (
    <div className="sidebar">
      <div className="brand">
        <div className="brand-icon">✦</div>
        <div>
          <div className="brand-name">NexusAI</div>
          <div className="brand-sub">Support</div>
        </div>
      </div>

      <div>
        <div className="sidebar-label">Status</div>
        <div className="sidebar-status">
          <div className="status-dot"></div>
          <div className="status-text">Agent is <span>Online</span></div>
        </div>
      </div>

      <div className="sidebar-footer">
        <div className="user-avatar">P</div>
        <div>
          <div className="user-name">Pranay</div>
          <div className="user-role">Member 1 · Core Chat</div>
        </div>
      </div>
    </div>
  );
}

export default Sidebar;