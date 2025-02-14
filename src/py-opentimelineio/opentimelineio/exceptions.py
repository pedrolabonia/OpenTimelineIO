# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the OpenTimelineIO project

"""Exception classes for OpenTimelineIO"""
from . _otio import ( # noqa
    OTIOError,
    NotAChildError,
    UnsupportedSchemaError,
    CannotComputeAvailableRangeError
)


class CouldNotReadFileError(OTIOError):
    pass


class NoKnownAdapterForExtensionError(OTIOError):
    pass


class ReadingNotSupportedError(OTIOError):
    pass


class WritingNotSupportedError(OTIOError):
    pass


class NotSupportedError(OTIOError):
    pass


class InvalidSerializableLabelError(OTIOError):
    pass


class AdapterDoesntSupportFunctionError(OTIOError):
    pass


class InstancingNotAllowedError(OTIOError):
    pass


class TransitionFollowingATransitionError(OTIOError):
    pass


class MisconfiguredPluginError(OTIOError):
    pass


class CannotTrimTransitionsError(OTIOError):
    pass


class NoDefaultMediaLinkerError(OTIOError):
    pass
