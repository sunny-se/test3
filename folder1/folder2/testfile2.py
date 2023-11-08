const { Octokit } = require("@octokit/rest");

const octokit = new Octokit({
  auth: "YOUR_GITHUB_TOKEN", // Replace with your GitHub token
});

const owner = "your_owner";
const repoName = "your_repo";
const baseCommit = "base_commit_sha"; // Replace with the SHA of the base commit
const headCommit = "head_commit_sha"; // Replace with the SHA of the head commit

async function getFilesStatusBetweenCommits() {
  try {
    // Compare the two commits to get the list of changes without diff data
    const comparison = await octokit.repos.compareCommits({
      owner,
      repo: repoName,
      base: baseCommit,
      head: headCommit,
    });

    // Extract the file changes and their statuses
    const changes = comparison.data.files.map((file) => {
      return {
        filename: file.filename,
        status: file.status,
      };
    });

    console.log("File changes and their statuses:");
    console.log(changes);
  } catch (error) {
    console.error("Error:", error);
  }
}

getFilesStatusBetweenCommits();
