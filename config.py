# =====================================================================
#  SOVEREIGN PIPELINE MATRIX ARCHITECTURE - CONFIGURATION
#  Copyright (c) 2026 BIREK. All Rights Reserved.
#  Licensed under the MIT License.
# =====================================================================

import logging
from enum import Enum
from dataclasses import dataclass
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PipelineState(Enum):
    """Enum for pipeline execution states"""
    ACTIVE = "ACTIVE"
    HALTED = "HALTED"
    DRIFT_DETECTED = "DRIFT_DETECTED"
    COLLAPSE = "COLLAPSE"
    ERROR = "ERROR"
    THREAD_FAULT = "THREAD_FAULT"


@dataclass
class PipelineConfig:
    """Configuration settings for Sovereign Pipeline"""
    # Anchor validation
    ANCHOR_LENGTH: int = 51
    ANCHOR_PREFIX: str = "12xbr"
    
    # Layer configuration
    LAYER_1_ANGLE: float = 45.0
    LAYER_2_ANGLE: float = 45.0
    
    # Resource management
    MACRO_RESOURCE_TIER: int = 10
    MACRO_RESOURCE_TIER_REDUCED: int = 5
    
    # Threading configuration
    MAX_WORKERS: int = 4
    THREAD_TIMEOUT: int = 30
    
    # Load intensity thresholds
    MIN_LOAD_INTENSITY: int = 1
    HIGH_LOAD_INTENSITY: int = 5
    
    # Mass retention
    LEFT_MASS_RETENTION: float = 50.0
    RIGHT_MASS_RETENTION: float = 50.0
    SOFTWARE_LEAKAGE_COEFFICIENT: float = 0.000000
    
    # Signature
    RAW_SIGNATURE: str = "BIREK_SOVEREIGN_ARCH_2026"
    
    # Center flow requirement
    CENTER_FLOW_REQUIRED: bool = True


# Global configuration instance
global_config = PipelineConfig()
