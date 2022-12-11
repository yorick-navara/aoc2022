from typing import Any, Dict, List, Tuple

from generic.read_inputs import read_csv_list_from_nr, read_input_df_from_nr

# class FileSystem():
#   dir_structure:Dict[str,Any] = {}
#   cwd:List[str] = []
#   curr_dir:Dict[str, Any] = dir_structure


def ls_from_path(
  dir_structure:Dict[str,Any],
  cwd:List[str]
) -> Dict[str, Any]:
  rel_dict = dir_structure
  for dir in cwd:
    rel_dict = rel_dict[dir]
  return rel_dict

def add_folder_to_path(
  dir_structure:Dict[str,Any], 
  cwd:List[str],
  new_dir:str
) -> None:
  curr_dir = ls_from_path(dir_structure, cwd)
  add_folder(curr_dir, new_dir)

def add_folder(curr_dir:Dict, new_dir:str):
  curr_dir[new_dir] = {}


def process_command(
  command:str,
  dir_structure:Dict[str,Any],
  cwd: List[str]) -> Tuple[Dict, List[str]]:
  # print(command)
  if command == 'cd /':
    dir_structure = {'/': {}}
    cwd = ['/']
    return dir_structure, cwd
  elif command == ('cd ..'):
    return dir_structure, cwd[:-1]
  elif command.startswith('cd '):
    new_dir = command[3:]
    add_folder_to_path(dir_structure, cwd, new_dir)
    cwd.append(new_dir)
    return dir_structure, cwd
  elif command == 'ls':
    return dir_structure, cwd
  else:
    return NotImplementedError(f'Command {command} not recognized')


def process_file_contents(line:str, dir_structure:Dict[str,Any], cwd:List[str]):
  # print("process_file_contents")
  split_line = line.split(' ') # expect form "1234 file.txt"

  curr_dir = ls_from_path(dir_structure, cwd)
  # print(split_line[0], split_line[1])
  if split_line[0].isdigit():
    curr_dir[split_line[1]] = int(split_line[0])
  else:
    curr_dir[split_line[1]] = split_line[0]


def get_folder_size_2(dir_structure: Dict[str, any], rel_path:str = '') -> Dict[str, int]:
  folder_sizes = {}
  cwd_str = rel_path
  for key in dir_structure:
    if isinstance(dir_structure[key], int):
      #cwd_str = cwd_str + '/' + key
      if cwd_str not in folder_sizes:
        folder_sizes[cwd_str] = dir_structure[key]  
      else:
        folder_sizes[cwd_str] += dir_structure[key]
    elif isinstance(dir_structure[key], dict):
      folder_sizes_2 = get_folder_size_2(dir_structure[key], rel_path=cwd_str + '/' + key)
      folder_sizes = {**folder_sizes, **folder_sizes_2}
  return folder_sizes


def get_folder_size(dir_structure: Dict[str, any]) -> Dict[str, int]:
  #print("get_folder_size")
  folder_sizes = {}
  for key in dir_structure:
    folders_applies = []
    #print(key, dir_structure[key])
    if isinstance(dir_structure[key], dict):
      folders_applies.append(key)
      folder_sizes = get_folder_size(dir_structure=dir_structure[key])
      #print(folder_sizes)
      size = sum([folder_sizes[x] for x in folder_sizes])
      #print(size)

      for folder in folders_applies:
        if folder not in folder_sizes.keys():
          folder_sizes[folder] = size
        else:
          folder_sizes[folder] += size
    else: # isinstance int
      file_size = dir_structure[key]
      for folder in folders_applies:
        if folder not in folder_sizes.keys():
          folder_sizes[folder] = file_size
        else:
          folder_sizes[folder] += file_size
    
    return folder_sizes


def determine_file_structure(input:List[str]) -> Dict[str, Any]:
  dir_structure = {}
  cwd = []
  curr_dirr = None
  for line in input:
    if line.startswith('$ '):
      dir_structure, cwd = process_command(line[2:], dir_structure, cwd)
    else:
      process_file_contents(line, dir_structure, cwd)
    #print(dir_structure, cwd)
  return dir_structure


def part1(use_example:bool=False):
  input = read_csv_list_from_nr(7, use_example=use_example)

  dir_structure = determine_file_structure(input)
  
  #print("dir_structure")
  #print(dir_structure)

  dir_sizes = get_folder_size_2(dir_structure)
  # print("dir_sizes")
  # print(dir_sizes)
  complete_dir_sizes = {}
  for file1 in dir_sizes:
    total = sum([dir_sizes[file] for file in dir_sizes if file.startswith(file1)])
    complete_dir_sizes[file1] = total
  # print("complete_dir_sizes")
  # print(complete_dir_sizes)
  max_size = 100000
  directories_small_enough = [complete_dir_sizes[dir] for dir in complete_dir_sizes if complete_dir_sizes[dir] <= max_size]
  #print(directories_small_enough)
  total_size = sum(directories_small_enough)
  return total_size


def part2(use_example:bool=False):
  input = read_csv_list_from_nr(7, use_example=use_example)
  return 42
