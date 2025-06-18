from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Severity(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


class Location(BaseModel):
    path: str
    start_line: int
    end_line: int
    start_column: Optional[int] = None
    end_column: Optional[int] = None


class Issue(BaseModel):
    check_id: str
    message: str
    severity: Severity
    location: Location
    description: str
    recommendation: str
    code_snippet: str
    metadata: Dict = Field(default_factory=dict)


class AnalysisResult(BaseModel):
    issues: List[Issue] = Field(default_factory=list)
    summary: Dict = Field(default_factory=dict)
    metadata: Dict = Field(default_factory=dict)

    def add_issue(self, issue: Issue) -> None:
        """Add an issue to the analysis result."""
        self.issues.append(issue)

    def get_issues_by_severity(self, severity: Severity) -> List[Issue]:
        """Get all issues of a specific severity."""
        return [issue for issue in self.issues if issue.severity == severity]

    def to_dict(self) -> Dict:
        """Convert the analysis result to a dictionary."""
        return {
            "issues": [issue.model_dump() for issue in self.issues],
            "summary": self.summary,
            "metadata": self.metadata,
        }

    def to_html(self) -> str:
        """Convert the analysis result to HTML format."""
        # TODO: Implement HTML conversion
        pass

    def to_json(self) -> str:
        """Convert the analysis result to JSON format."""
        return self.model_dump_json(indent=2) 