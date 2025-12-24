from server import mcp
import tools.file_search_tool
import resources.file_resources
import resources.prompt_resources

if __name__ == "__main__":

    mcp.run(transport="streamable-http")