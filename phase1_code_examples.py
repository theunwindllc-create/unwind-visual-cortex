#!/usr/bin/env python3
"""
Phase 1 Integration - Code Examples
Practical, working examples for Pexels + AE JSON integration

These examples can be copied and used directly in your projects.
"""

import os
import json
from typing import List, Dict, Optional
from datetime import datetime


# ============================================================================
# EXAMPLE 1: Simple B-Roll Download
# ============================================================================

def example_simple_broll_download():
    """
    Simplest possible B-roll download example
    Downloads one video and saves it to current directory
    """
    from pexels_integration import search_and_download_broll
    
    # One-line download
    video_path = search_and_download_broll("business meeting")
    
    if video_path:
        print(f"✓ Video downloaded: {video_path}")
    else:
        print("✗ No video found")
    
    return video_path


# ============================================================================
# EXAMPLE 2: Download Multiple B-Roll Clips
# ============================================================================

def example_batch_broll_download(shot_descriptions: List[str], output_dir: str = "./broll"):
    """
    Download multiple B-roll clips for a shot list
    
    Args:
        shot_descriptions: List of shot descriptions
        output_dir: Where to save videos
    
    Returns:
        List of successfully downloaded video paths
    """
    from pexels_integration import search_and_download_broll
    
    os.makedirs(output_dir, exist_ok=True)
    downloaded = []
    
    print(f"Downloading {len(shot_descriptions)} B-roll clips...")
    
    for i, description in enumerate(shot_descriptions, 1):
        print(f"[{i}/{len(shot_descriptions)}] {description}")
        
        try:
            video_path = search_and_download_broll(
                shot_description=description,
                output_dir=output_dir,
                orientation="landscape",
                quality="hd"
            )
            
            if video_path:
                downloaded.append(video_path)
                print(f"  ✓ {os.path.basename(video_path)}")
            else:
                print(f"  ⚠ No suitable video found")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print(f"\n✓ Downloaded {len(downloaded)}/{len(shot_descriptions)} videos")
    return downloaded


# ============================================================================
# EXAMPLE 3: Advanced Pexels Search with Filters
# ============================================================================

def example_advanced_pexels_search(query: str, min_duration: int = 5, max_duration: int = 30):
    """
    Advanced Pexels search with duration filters
    
    Args:
        query: Search query
        min_duration: Minimum video duration in seconds
        max_duration: Maximum video duration in seconds
    
    Returns:
        Video metadata dictionary or None
    """
    from pexels_integration import PexelsClient
    
    client = PexelsClient()
    
    # Find best match with filters
    video = client.find_best_match(
        query=query,
        orientation="landscape",
        min_duration=min_duration,
        max_duration=max_duration
    )
    
    if video:
        print(f"Found video:")
        print(f"  ID: {video['id']}")
        print(f"  Duration: {video['duration']}s")
        print(f"  Resolution: {video['width']}x{video['height']}")
        print(f"  User: {video['user']['name']}")
        
        # Get download URL
        video_url = client.get_video_file_url(video, quality="hd")
        print(f"  Download URL: {video_url}")
        
        return video
    else:
        print("No video found matching criteria")
        return None


# ============================================================================
# EXAMPLE 4: Simple AE JSON Conversion
# ============================================================================

def example_simple_ae_json_conversion(blueprint_path: str, output_path: str = "./ae_data.json"):
    """
    Convert blueprint to AE JSON - simplest example
    
    Args:
        blueprint_path: Path to Unwind blueprint JSON
        output_path: Where to save AE JSON
    
    Returns:
        Path to generated AE JSON file
    """
    from ae_json_exporter import convert_blueprint_to_ae_json
    
    # One-line conversion
    ae_json_path = convert_blueprint_to_ae_json(
        blueprint_path=blueprint_path,
        output_path=output_path,
        pretty=True
    )
    
    print(f"✓ AE JSON created: {ae_json_path}")
    print(f"  Import this file into After Effects as footage")
    
    return ae_json_path


# ============================================================================
# EXAMPLE 5: Custom AE JSON with Additional Data
# ============================================================================

def example_custom_ae_json(blueprint_path: str, custom_data: Dict):
    """
    Create AE JSON with custom additional data
    
    Args:
        blueprint_path: Path to blueprint
        custom_data: Additional data to include in JSON
    
    Returns:
        Path to AE JSON file
    """
    from ae_json_exporter import AEJSONExporter
    import json
    
    # Load blueprint
    with open(blueprint_path, 'r') as f:
        blueprint = json.load(f)
    
    # Create exporter
    exporter = AEJSONExporter(blueprint)
    
    # Convert to AE JSON
    ae_data = exporter.convert()
    
    # Add custom data
    ae_data['custom_data'] = custom_data
    ae_data['custom_data']['generated_by'] = 'Unwind Visual Cortex'
    ae_data['custom_data']['timestamp'] = datetime.now().isoformat()
    
    # Save
    output_path = "./ae_data_custom.json"
    with open(output_path, 'w') as f:
        json.dump(ae_data, f, indent=2)
    
    print(f"✓ Custom AE JSON created: {output_path}")
    return output_path


# ============================================================================
# EXAMPLE 6: Complete Project Setup
# ============================================================================

def example_complete_project_setup(
    project_name: str,
    shot_descriptions: List[str],
    brand_colors: Dict[str, str],
    base_dir: str = "/home/ubuntu/projects"
):
    """
    Complete project setup with directory structure and assets
    
    Args:
        project_name: Name of the project
        shot_descriptions: List of B-roll shot descriptions
        brand_colors: Dictionary of brand colors (hex format)
        base_dir: Base directory for projects
    
    Returns:
        Dictionary with project information
    """
    from pexels_integration import search_and_download_broll
    
    # Create project directory structure
    project_dir = os.path.join(base_dir, project_name.replace(' ', '_').lower())
    broll_dir = os.path.join(project_dir, 'broll')
    exports_dir = os.path.join(project_dir, 'exports')
    templates_dir = os.path.join(project_dir, 'templates')
    
    for directory in [project_dir, broll_dir, exports_dir, templates_dir]:
        os.makedirs(directory, exist_ok=True)
    
    print(f"Created project structure: {project_dir}")
    
    # Create minimal blueprint
    blueprint = {
        'project_metadata': {
            'project_name': project_name,
            'created_date': datetime.now().isoformat(),
            'platform': 'all',
            'conversion_goal': 'leads'
        },
        'brand_analysis': {
            'brand_name': project_name,
            'brand_colors': brand_colors
        },
        'visual_recommendations': {
            'shot_list': [
                {'description': desc, 'duration': 5}
                for desc in shot_descriptions
            ]
        },
        'emotional_tone_mapping': {
            'overall_tone': 'professional',
            'pacing': 'moderate'
        }
    }
    
    # Save blueprint
    blueprint_path = os.path.join(project_dir, 'blueprint.json')
    with open(blueprint_path, 'w') as f:
        json.dump(blueprint, f, indent=2)
    
    print(f"✓ Blueprint created: {blueprint_path}")
    
    # Download B-roll
    print(f"\nDownloading {len(shot_descriptions)} B-roll clips...")
    broll_assets = []
    
    for i, description in enumerate(shot_descriptions, 1):
        print(f"[{i}/{len(shot_descriptions)}] {description}")
        
        try:
            video_path = search_and_download_broll(
                shot_description=description,
                output_dir=broll_dir,
                orientation="landscape",
                quality="hd"
            )
            
            if video_path:
                broll_assets.append({
                    'shot_number': i,
                    'description': description,
                    'path': video_path,
                    'filename': os.path.basename(video_path)
                })
                print(f"  ✓ {os.path.basename(video_path)}")
            else:
                print(f"  ⚠ No video found")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    # Update blueprint with assets
    blueprint['broll_assets'] = broll_assets
    with open(blueprint_path, 'w') as f:
        json.dump(blueprint, f, indent=2)
    
    # Generate AE JSON
    from ae_json_exporter import convert_blueprint_to_ae_json
    
    ae_json_path = convert_blueprint_to_ae_json(
        blueprint_path=blueprint_path,
        output_path=os.path.join(project_dir, 'ae_data.json'),
        pretty=True
    )
    
    print(f"\n✓ AE JSON created: {ae_json_path}")
    
    # Create project summary
    summary = {
        'project_name': project_name,
        'project_dir': project_dir,
        'created_date': datetime.now().isoformat(),
        'blueprint_path': blueprint_path,
        'ae_json_path': ae_json_path,
        'broll_count': len(broll_assets),
        'broll_assets': broll_assets,
        'directories': {
            'broll': broll_dir,
            'exports': exports_dir,
            'templates': templates_dir
        },
        'status': 'ready_for_editing'
    }
    
    summary_path = os.path.join(project_dir, 'PROJECT_SUMMARY.json')
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"PROJECT SETUP COMPLETE")
    print(f"{'='*60}")
    print(f"Project: {project_name}")
    print(f"Directory: {project_dir}")
    print(f"B-roll clips: {len(broll_assets)}")
    print(f"Blueprint: {blueprint_path}")
    print(f"AE JSON: {ae_json_path}")
    print(f"Summary: {summary_path}")
    print(f"{'='*60}")
    
    return summary


# ============================================================================
# EXAMPLE 7: Validate Project Assets
# ============================================================================

def example_validate_project(project_dir: str):
    """
    Validate that all project assets are present and valid
    
    Args:
        project_dir: Path to project directory
    
    Returns:
        Validation results dictionary
    """
    results = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'assets': {}
    }
    
    print(f"Validating project: {project_dir}\n")
    
    # Check directory exists
    if not os.path.exists(project_dir):
        results['valid'] = False
        results['errors'].append(f"Project directory not found: {project_dir}")
        return results
    
    # Check blueprint
    blueprint_path = os.path.join(project_dir, 'blueprint.json')
    if os.path.exists(blueprint_path):
        print("✓ Blueprint found")
        results['assets']['blueprint'] = blueprint_path
        
        # Validate JSON
        try:
            with open(blueprint_path, 'r') as f:
                blueprint = json.load(f)
            print("  ✓ Valid JSON")
            
            # Check required sections
            required = ['brand_analysis', 'visual_recommendations']
            for section in required:
                if section in blueprint:
                    print(f"  ✓ Section '{section}' present")
                else:
                    results['warnings'].append(f"Blueprint missing section: {section}")
                    print(f"  ⚠ Section '{section}' missing")
                    
        except json.JSONDecodeError as e:
            results['valid'] = False
            results['errors'].append(f"Blueprint JSON invalid: {e}")
            print(f"  ✗ Invalid JSON: {e}")
    else:
        results['valid'] = False
        results['errors'].append("Blueprint file missing")
        print("✗ Blueprint not found")
    
    # Check AE JSON
    ae_json_path = os.path.join(project_dir, 'ae_data.json')
    if os.path.exists(ae_json_path):
        print("✓ AE JSON found")
        results['assets']['ae_json'] = ae_json_path
    else:
        results['warnings'].append("AE JSON file missing")
        print("⚠ AE JSON not found")
    
    # Check B-roll directory
    broll_dir = os.path.join(project_dir, 'broll')
    if os.path.exists(broll_dir):
        videos = [f for f in os.listdir(broll_dir) if f.endswith('.mp4')]
        results['assets']['broll_count'] = len(videos)
        results['assets']['broll_files'] = videos
        print(f"✓ B-roll directory found ({len(videos)} videos)")
        
        if len(videos) == 0:
            results['warnings'].append("No B-roll videos found")
            print("  ⚠ No videos in directory")
    else:
        results['warnings'].append("B-roll directory missing")
        print("⚠ B-roll directory not found")
    
    # Summary
    print(f"\n{'='*60}")
    if results['valid']:
        print("✓ PROJECT VALID")
    else:
        print("✗ PROJECT INVALID")
    
    if results['errors']:
        print(f"\nErrors ({len(results['errors'])}):")
        for error in results['errors']:
            print(f"  ✗ {error}")
    
    if results['warnings']:
        print(f"\nWarnings ({len(results['warnings'])}):")
        for warning in results['warnings']:
            print(f"  ⚠ {warning}")
    
    print(f"{'='*60}")
    
    return results


# ============================================================================
# EXAMPLE 8: Parallel B-Roll Download (Fast)
# ============================================================================

def example_parallel_broll_download(shot_descriptions: List[str], output_dir: str = "./broll"):
    """
    Download multiple B-roll clips in parallel for faster processing
    
    Args:
        shot_descriptions: List of shot descriptions
        output_dir: Where to save videos
    
    Returns:
        List of downloaded video paths
    """
    from pexels_integration import PexelsClient
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import time
    
    os.makedirs(output_dir, exist_ok=True)
    client = PexelsClient()
    
    def download_single(description):
        """Download a single B-roll clip"""
        try:
            # Find best match
            video = client.find_best_match(
                query=description,
                orientation="landscape",
                min_duration=5
            )
            
            if not video:
                return None, description, "No video found"
            
            # Get download URL
            video_url = client.get_video_file_url(video, quality="hd")
            if not video_url:
                return None, description, "No download URL"
            
            # Download
            filename = f"{description[:30].replace(' ', '_')}_{video['id']}.mp4"
            output_path = os.path.join(output_dir, filename)
            
            result = client.download_video(video_url, output_path)
            return result, description, "Success"
            
        except Exception as e:
            return None, description, str(e)
    
    print(f"Downloading {len(shot_descriptions)} B-roll clips in parallel...")
    start_time = time.time()
    
    # Download in parallel (max 5 concurrent to respect rate limits)
    downloaded = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Submit all tasks
        future_to_desc = {
            executor.submit(download_single, desc): desc 
            for desc in shot_descriptions
        }
        
        # Process as they complete
        for i, future in enumerate(as_completed(future_to_desc), 1):
            path, description, status = future.result()
            
            if path:
                downloaded.append(path)
                print(f"[{i}/{len(shot_descriptions)}] ✓ {description}")
            else:
                print(f"[{i}/{len(shot_descriptions)}] ✗ {description} ({status})")
    
    elapsed = time.time() - start_time
    
    print(f"\n✓ Downloaded {len(downloaded)}/{len(shot_descriptions)} videos")
    print(f"  Time: {elapsed:.1f}s ({elapsed/len(shot_descriptions):.1f}s per video)")
    
    return downloaded


# ============================================================================
# MAIN - Run Examples
# ============================================================================

if __name__ == "__main__":
    print("Phase 1 Integration - Code Examples")
    print("="*60)
    print("\nAvailable examples:")
    print("1. Simple B-roll download")
    print("2. Batch B-roll download")
    print("3. Advanced Pexels search")
    print("4. Simple AE JSON conversion")
    print("5. Custom AE JSON")
    print("6. Complete project setup")
    print("7. Validate project")
    print("8. Parallel B-roll download")
    print("\nTo run an example, uncomment the corresponding function call below.")
    print("="*60)
    
    # Example 1: Simple download
    # example_simple_broll_download()
    
    # Example 2: Batch download
    # shots = ["business meeting", "city skyline", "coffee shop"]
    # example_batch_broll_download(shots, "./test_broll")
    
    # Example 3: Advanced search
    # example_advanced_pexels_search("ocean waves", min_duration=10, max_duration=20)
    
    # Example 4: Simple AE JSON
    # example_simple_ae_json_conversion("./blueprint.json", "./ae_data.json")
    
    # Example 5: Custom AE JSON
    # custom_data = {'template_version': '1.0', 'editor': 'John Doe'}
    # example_custom_ae_json("./blueprint.json", custom_data)
    
    # Example 6: Complete project setup
    # example_complete_project_setup(
    #     project_name="TechFlow Product Launch",
    #     shot_descriptions=["business meeting", "laptop work", "city skyline"],
    #     brand_colors={'primary': '#0066FF', 'secondary': '#00CC88'}
    # )
    
    # Example 7: Validate project
    # example_validate_project("/home/ubuntu/projects/techflow_product_launch")
    
    # Example 8: Parallel download
    # shots = ["business meeting", "city skyline", "coffee shop", "handshake"]
    # example_parallel_broll_download(shots, "./test_broll_parallel")
    
    print("\n✓ Examples ready to use!")
    print("Edit this file to uncomment and run specific examples.")
