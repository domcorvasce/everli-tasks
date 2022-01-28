<?php

/**
 * Represents a path of an abstract file system based on Unix's.
 */
class Path {
  // Current working directory (e.g. '/usr/bin')
  public string $currentPath;

  /**
   * Initializes a new path object.
   *
   * @param string $cwd Initial path for the working directory
   */
  public function __construct(string $cwd = '/')
  {
    $this->currentPath = $cwd;
  }

  /**
   * Changes the current working directory.
   *
   * @param string $path Path to the next working directory (relative or absolute)
   */
  public function cd(string $path)
  {
    $isAbsolutePath = $path[0] === '/';

    // If the user passed an absolute path
    // then just change the current working directory to match it
    if ($isAbsolutePath) {
      $this->currentPath = $path;
      return;
    }

    $this->computeWorkingDirectory($path);
  }

  /**
   * Computes the next working directory based on the current working directory
   * and a given relative path.
   *
   * @param string $relativePath Relative path
   */
  private function computeWorkingDirectory(string $relativePath)
  {
    $cwdDirs = explode('/', $this->currentPath);
    $relativePathDirs = explode('/', $relativePath);

    // Iterate over each directory that makes up the relative path
    // in order to compute the next working directory
    foreach ($relativePathDirs as $dir) {
      // Move to a child of the current working directory
      if ($dir !== '..') {
        $cwdDirs[] = $dir;
        continue;
      }

      // Pop off a directory so the cwd points to its parent
      array_pop($cwdDirs);
    }

    $this->currentPath = implode('/', $cwdDirs);
  }
}

$path = new Path('/a/b/c/d');
$path->cd('/usr/local/bin');

assert($path->currentPath === '/usr/local/bin');

$path->cd('/a/b/c/d');
$path->cd('../x');

assert($path->currentPath === '/a/b/c/x');
