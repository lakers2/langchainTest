from typing import Annotated, List, TypedDict
from pydantic import BaseModel, Field
from enum import Enum
import operator

class Section(BaseModel):
    name: str = Field(
        description = "Name for the section report."
    )
    description: str = Field(
        description = "Brief overview of the main topics and concepts to be covered in this section."
    )
    content: str = Field(
        description = "Whether to perform web research for this section of the report."
    )
    research: str = Field(
        description = "The content of the section."
    )
    
class Sections(BaseModel):
    sections: List[Section] = Field(
        description = "A list of sections for the report."
    )

class SerachQuery(BaseModel):
    search_query: str = Field(
        None,
        description = "The search query to be used for the web research."
    )

class Queries(BaseModel):
    queries: List[SerachQuery] = Field(
        description="List of search queries."
    )

class ReportStateInput(TypedDict):
    topic: str
    feedback_on_report_plan: str
    accept_report_plan: bool
    
class ReportStateOutput(TypedDict):
    final_report: str

class ReportState(TypedDict):
    topic: str
    feedback_on_report_plan: str
    accept_report_plan: bool
    queries: List[SerachQuery]
    sections: List[Section]
    completed_sections: Annotated[list, operator.add]
    final_report: str

class SectionState(TypedDict):
    section: Section
    completed_sections: Annotated[list, operator.add]
    search_queries: list[SerachQuery]
    source_str: str
    report_sections_from_research: str

class SectionOutputState(TypedDict):
    completed_sections: Annotated[list, operator.add]

    