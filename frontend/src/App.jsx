import { useState } from "react";
import axios from "axios";
import { Button, TextField, Typography, Container, Paper, List, ListItem, CircularProgress } from "@mui/material";

function App() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [message, setMessage] = useState("");
  const [matchScore, setMatchScore] = useState(null);
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file || !jobDescription) {
      setMessage("Please select a file and enter a job description.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_description", jobDescription);

    try {
      const response = await axios.post("http://3.142.199.10:5001/analyze", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });

      setMessage(`Analysis Complete: ${response.data.message}`);
      setMatchScore(response.data.match_score);
      setSkills(response.data.extracted_skills);
    } catch (error) {
      setMessage("Upload failed. Please try again.");
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="sm" style={{ textAlign: "center", marginTop: "50px" }}>
      <Paper elevation={3} style={{ padding: "20px" }}>
        <Typography variant="h4" gutterBottom>
          AI Resume Analyzer
        </Typography>

        <TextField
          label="Enter Job Description"
          multiline
          rows={4}
          fullWidth
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          style={{ marginBottom: "15px" }}
        />

        <input type="file" onChange={handleFileChange} style={{ marginBottom: "15px" }} />
        <br />
        <Button variant="contained" color="primary" onClick={handleUpload} disabled={loading}>
          {loading ? <CircularProgress size={24} /> : "Upload"}
        </Button>

        <Typography variant="body1" style={{ marginTop: "15px" }}>
          {message}
        </Typography>

        {matchScore !== null && (
          <div>
            <Typography variant="h5" style={{ marginTop: "20px" }}>
              Job Match Score: {matchScore}%
            </Typography>
            <Typography variant="h6" style={{ marginTop: "10px" }}>
              Extracted Skills:
            </Typography>
            <List>
              {skills.map((skill, index) => (
                <ListItem key={index}>{skill}</ListItem>
              ))}
            </List>
          </div>
        )}
      </Paper>
    </Container>
  );
}

export default App;
