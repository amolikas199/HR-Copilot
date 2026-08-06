import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const API = 'http://localhost:8000';

export default function App() {
  const [tab, setTab] = useState('home');
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [confidence, setConfidence] = useState('');
  const [sources, setSources] = useState([]);
  const [checklist, setChecklist] = useState('');
  const [leaveText, setLeaveText] = useState('');
  const [leaveData, setLeaveData] = useState('');
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post(`${API}/ask`, { question });
      setAnswer(res.data.answer);
      setConfidence(res.data.confidence);
      setSources(res.data.sources);
    } catch (e) {
      setAnswer('Error: Could not reach server');
    }
    setLoading(false);
  };

  const generateChecklist = async () => {
    setLoading(true);
    try {
      const res = await axios.post(`${API}/checklist`);
      setChecklist(res.data.checklist);
    } catch (e) {
      setChecklist('Error generating checklist');
    }
    setLoading(false);
  };

  const extractLeave = async () => {
    if (!leaveText.trim()) return;
    setLoading(true);
    try {
      const res = await axios.post(`${API}/extract-leave`, { sentence: leaveText });
      setLeaveData(JSON.stringify(res.data, null, 2));
    } catch (e) {
      setLeaveData('Error extracting leave');
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <nav className="nav">
        <h1>💼 HR Copilot</h1>
        <div className="tabs">
          <button className={tab === 'home' ? 'active' : ''} onClick={() => setTab('home')}>Home</button>
          <button className={tab === 'knowledge' ? 'active' : ''} onClick={() => setTab('knowledge')}>📚 Knowledge</button>
          <button className={tab === 'onboarding' ? 'active' : ''} onClick={() => setTab('onboarding')}>🧭 Onboarding</button>
          <button className={tab === 'leave' ? 'active' : ''} onClick={() => setTab('leave')}>📝 Leave</button>
        </div>
      </nav>

      <main className="container">
        {tab === 'home' && (
          <div className="card">
            <h2>Welcome to HR Copilot</h2>
            <p>An AI HR assistant for policy Q&A, onboarding, and leave requests.</p>
            <ul>
              <li>📚 Ask HR policy questions</li>
              <li>🧭 Generate onboarding checklists</li>
              <li>📝 Extract leave requests</li>
            </ul>
          </div>
        )}

        {tab === 'knowledge' && (
          <div className="card">
            <h2>Knowledge Assistant</h2>
            <input type="text" placeholder="Ask a policy question..." value={question} onChange={(e) => setQuestion(e.target.value)} />
            <button onClick={askQuestion} disabled={loading}>{loading ? 'Loading...' : 'Ask'}</button>
            {answer && (
              <>
                <div className="result">
                  <h3>Answer</h3>
                  <p>{answer}</p>
                  <p className="meta">Confidence: {confidence}%</p>
                  {sources.length > 0 && (
                    <div>
                      <strong>Sources:</strong>
                      <ul>
                        {sources.map((src, i) => <li key={i}>{src[0]} (page {src[1]})</li>)}
                      </ul>
                    </div>
                  )}
                </div>
              </>
            )}
          </div>
        )}

        {tab === 'onboarding' && (
          <div className="card">
            <h2>Onboarding Checklist</h2>
            <button onClick={generateChecklist} disabled={loading}>{loading ? 'Generating...' : 'Generate Checklist'}</button>
            {checklist && (
              <div className="result">
                <pre>{checklist}</pre>
              </div>
            )}
          </div>
        )}

        {tab === 'leave' && (
          <div className="card">
            <h2>Leave Request</h2>
            <textarea placeholder="E.g., I need leave from 12th to 16th for medical reasons" value={leaveText} onChange={(e) => setLeaveText(e.target.value)} />
            <button onClick={extractLeave} disabled={loading}>{loading ? 'Processing...' : 'Extract'}</button>
            {leaveData && (
              <div className="result">
                <pre>{leaveData}</pre>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}
